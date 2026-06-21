class SecuritySystem:
    HW_OK = True
    SW_INTEGRITY_OK = True
    NET_CONNECTED = True

    @staticmethod
    def check_conditions(conditions):
        all_true = True
        for condition in conditions:
            if not all(condition):
                all_true = False
                break
        return all_true

if __name__ == '__main__':
    hardware_status = [SecuritySystem.HW_OK, SecuritySystem.HW_OK]
    software_integrity = [SecuritySystem.SW_INTEGRITY_OK, SecuritySystem.SW_INTEGRITY_OK]
    network_connectivity = [SecuritySystem.NET_CONNECTED, SecuritySystem.NET_CONNECTED]

    conditions = [
        (hardware_status[0], software_integrity[0]),
        (network_connectivity[1])
    ]

    result = SecuritySystem.check_conditions(conditions)
    print(result)