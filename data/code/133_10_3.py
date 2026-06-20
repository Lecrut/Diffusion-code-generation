def evaluate_nested_logic():
    logic_map = {
        'A': True,
        'B': False,
        'C': True,
        'D': False,
        'E': (True and False) or (not True),
        'F': (False and True) or (not False)
    }
    
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