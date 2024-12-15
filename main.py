from scapy.all import sniff
import psutil

def list_network_interfaces():
    print("Available network interfaces:")
    interfaces = psutil.net_if_addrs()
    for idx, interface in enumerate(interfaces.keys(), start=1):
        print(f"{idx}. {interface}")

def get_selected_interface():
    list_network_interfaces()
    choice = input("Select a network interface by number: ")
    try:
        choice = int(choice)
        interfaces = list(psutil.net_if_addrs().keys())
        if 1 <= choice <= len(interfaces):
            return interfaces[choice - 1]
        else:
            print("Invalid choice, using default interface.")
            return None  # Varsayılan arayüz
    except ValueError:
        print("Invalid input. Using default interface.")
        return None  

def packet_callback(packet):
    print(f"Packet captured: {packet.summary()}")

def start_sniffing(interface=None):
    print(f"Starting packet sniffing on interface: {interface or 'default'}")
    sniff(prn=packet_callback, store=0, iface=interface)

if __name__ == "__main__":
    interface = get_selected_interface()
    start_sniffing(interface)
