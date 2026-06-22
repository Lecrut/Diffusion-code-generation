def validate_and_gate(a, b):
    truth_table = {
        (False, False): False,
        (False, True): False,
        (True, False): False,
        (True, True): True
    }
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values")
    return truth_table[(a, b)]

if __name__ == '__main__':
    val1 = True
    val2 = True
    print(validate_and_gate(val1, val2))