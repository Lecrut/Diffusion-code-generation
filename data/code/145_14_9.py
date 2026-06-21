def evaluate_security_state(hardware_status, software_integrity, network_connectivity):
    if not hardware_status:
        return "Hardware Failure"
    if not software_integrity:
        return "Software Integrity Issue"
    if not network_connectivity:
        return "Network Connectivity Problem"
    return "System is Secure"

if __name__ == '__main__':
    hw = True
    sw = False
    nc = True
    state = evaluate_security_state(hw, sw, nc)
    print(state)