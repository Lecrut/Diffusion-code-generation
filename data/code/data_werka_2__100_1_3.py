def check_logic(A, B, C):
    truth_table = {
        (True, True, True): True,
        (True, True, False): True,
        (True, False, True): False,
        (True, False, False): True,
        (False, True, True): False,
        (False, True, False): False,
        (False, False, True): False,
        (False, False, False): False,
    }
    return truth_table[(A, B, C)]

if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    result = check_logic(A_val, B_val, C_val)
    print(result)