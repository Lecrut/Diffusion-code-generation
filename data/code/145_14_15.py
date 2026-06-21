def validate_conditions(variables, conditions):
    if not isinstance(variables, list) or len(variables) == 0:
        raise ValueError("Variables must be a non-empty list")
    
    if not all(isinstance(condition, tuple) and all(isinstance(var, int) and var < len(variables) for var in condition) for condition in conditions):
        raise ValueError("Conditions must be a list of tuples with valid variable indices")

def check_security_state(hardware_status, software_integrity, network_connectivity):
    return all([hardware_status, software_integrity, network_connectivity])

if __name__ == '__main__':
    variables = [True, False, True]
    conditions = [
        (0,), 
        (1,), 
        (2,)
    ]
    
    try:
        validate_conditions(variables, conditions)
        security_state = check_security_state(*[variables[var] for var in sum(conditions, [])])
        print(security_state)
    except ValueError as e:
        print(e)