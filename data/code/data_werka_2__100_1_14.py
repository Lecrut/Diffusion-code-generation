def check_logic(A, B, C):
    if not isinstance(A, bool) or not isinstance(B, bool) or not isinstance(C, bool):
        raise ValueError("Inputs must be boolean")
    cache = {
        (True, True, True): True,
        (True, True, False): True,
        (True, False, True): False,
        (True, False, False): True,
        (False, True, True): False,
        (False, True, False): False,
        (False, False, True): False,
        (False, False, False): False,
    }
    return cache[(A, B, C)]

if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = True
    computed = check_logic(val_a, val_b, val_c)
    print(computed)