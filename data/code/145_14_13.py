def evaluate_security_state(hardware_status, software_integrity, network_connectivity):
    if not isinstance(hardware_status, bool) or not isinstance(software_integrity, bool) or not isinstance(network_connectivity, bool):
        raise ValueError("All inputs must be boolean values.")
    
    if hardware_status and software_integrity and network_connectivity:
        return "System is secure"
    else:
        return "System is compromised"

if __name__ == '__main__':
    hardware = True
    software = False
    network = True
    
    try:
        result = evaluate_security_state(hardware, software, network)
        print(result)
    except ValueError as e:
        print(e)