def evaluate_security_system(hardware_status, software_integrity, network_connectivity):
    if hardware_status and software_integrity and network_connectivity:
        return "System is fully secure"
    elif not hardware_status:
        return "Hardware failure detected"
    elif not software_integrity:
        return "Software integrity compromised"
    else:
        return "Network connectivity issues"

if __name__ == '__main__':
    print(evaluate_security_system(True, True, True))
    print(evaluate_security_system(False, True, True))
    print(evaluate_security_system(True, False, True))
    print(evaluate_security_system(True, True, False))