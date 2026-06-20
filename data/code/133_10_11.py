def evaluate_complex_logic():
    logic_map = {
        'A': True,
        'B': False,
        'C': True,
        'D': False,
        'E': (True and False) or (not True),
        'F': (False and True) or (not False)
    }
    
    intermediate1 = logic_map['A'] and logic_map['B']
    intermediate2 = not logic_map['C'] and logic_map['D']
    intermediate3 = logic_map['E'] and logic_map['F']
    
    result = intermediate1 or intermediate2 or intermediate3
    return result

if __name__ == '__main__':
    print(evaluate_complex_logic())