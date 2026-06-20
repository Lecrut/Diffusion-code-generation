def evaluate_nested_logic(a, b, c, d):
    return (a and b) or (c and not d)

if __name__ == '__main__':
    logic_values = {
        'A': True,
        'B': False,
        'C': True,
        'D': False
    }
    result = evaluate_nested_logic(logic_values['A'], logic_values['B'], logic_values['C'], logic_values['D'])
    print(result)