def check_logic(A, B, C):
    return A and (B or not C)

if __name__ == '__main__':
    logic_results = {
        'A=True, B=False, C=True': check_logic(True, False, True),
        'A=True, B=True, C=False': check_logic(True, True, False),
        'A=False, B=True, C=False': check_logic(False, True, False),
        'A=False, B=False, C=True': check_logic(False, False, True)
    }
    
    for key, value in logic_results.items():
        print(f'{key}: {value}')