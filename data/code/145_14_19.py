class SecuritySystem:
    def __init__(self, hardware_status, software_integrity, network_connectivity):
        self.hardware_status = hardware_status
        self.software_integrity = software_integrity
        self.network_connectivity = network_connectivity

    def is_system_secure(self):
        return (self.hardware_status and
                self.software_integrity and
                self.network_connectivity)

if __name__ == '__main__':
    system = SecuritySystem(hardware_status=True, 
                             software_integrity=False, 
                             network_connectivity=True)
    print(system.is_system_secure())