def evaluate_nested_logic():
    logic_map = {
        'A': True,
        'B': False,
        'C': True,
        'D': False,
        'E': (True and False) or (not True),
        'F': (False and True) or (not False)
    }
    
    def validate_logic_map():
        if not isinstance(logic_map, dict):
            raise ValueError("logic_map must be a dictionary")
        for key, value in logic_map.items():
            if key not in ['A', 'B', 'C', 'D', 'E', 'F']:
                raise KeyError(f"Invalid key {key} in logic_map")
            if not isinstance(value, bool):
                raise ValueError(f"Value of {key} must be a boolean")
    
    validate_logic_map()
    
    result = (
        logic_map['A'] and logic_map['B']
    ) or (
        not logic_map['C'] and logic_map['D']
    ) or (
        logic_map['E'] and logic_map['F']
    )
    return result

if __name__ == '__main__':
    print(evaluate_nested_logic())