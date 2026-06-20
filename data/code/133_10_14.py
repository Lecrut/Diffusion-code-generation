logic_map = {
    'A': True,
    'B': False,
    'C': True,
    'D': False,
    'E': (True and False) or (not True),
    'F': (False and True) or (not False)
}

def evaluate_nested_logic(logic):
    return (
        logic_map['A'] and logic_map['B']
    ) or (
        not logic_map['C'] and logic_map['D']
    ) or (
        logic_map['E'] and logic_map['F']
    )

if __name__ == '__main__':
    result = evaluate_nested_logic(logic_map)
    print(result)