def evaluate_security_system(hardware_status, software_integrity, network_connectivity):
    security_levels = {
        'low': (False, True, False),
        'medium': (True, False, True),
        'high': (True, True, True)
    }
    
    for level, conditions in security_levels.items():
        if (hardware_status == conditions[0] and 
            software_integrity == conditions[1] and 
            network_connectivity == conditions[2]):
            return level

if __name__ == '__main__':
    hardware = True
    software = False
    network = True
    
    result = evaluate_security_system(hardware, software, network)
    print(result)