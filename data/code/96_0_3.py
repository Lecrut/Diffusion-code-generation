def evaluate_nested_logic(a, b, c, d):
    return (a and b) or (c and not d)

if __name__ == '__main__':
    logic_map = {
        'A': True,
        'B': False,
        'C': True,
        'D': False
    }
    result = evaluate_nested_logic(logic_map['A'], logic_map['B'], logic_map['C'], logic_map['D'])
    print(result)