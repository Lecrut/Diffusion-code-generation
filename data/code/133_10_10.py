LOGIC_MAP = {
    'A': True,
    'B': False,
    'C': True,
    'D': False,
    'E': (True and False) or (not True),
    'F': (False and True) or (not False)
}

def evaluate_nested_logic():
    result = (
        LOGIC_MAP['A'] and LOGIC_MAP['B']
    ) or (
        not LOGIC_MAP['C'] and LOGIC_MAP['D']
    ) or (
        LOGIC_MAP['E'] and LOGIC_MAP['F']
    )
    return result

if __name__ == '__main__':
    print(evaluate_nested_logic())