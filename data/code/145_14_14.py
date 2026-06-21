class SecuritySystem:
    def __init__(self, hardware_status, software_integrity, network_connectivity):
        self.hardware_status = hardware_status
        self.software_integrity = software_integrity
        self.network_connectivity = network_connectivity

    def is_secure(self):
        return self.hardware_status and self.software_integrity and self.network_connectivity

if __name__ == '__main__':
    system = SecuritySystem(True, False, True)
    print(system.is_secure())