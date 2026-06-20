def check_logic(A, B, C):
    return A and (B or not C)

if __name__ == '__main__':
    logic_values = {
        'A': True,
        'B': False,
        'C': True
    }
    result = check_logic(logic_values['A'], logic_values['B'], logic_values['C'])
    print(result)