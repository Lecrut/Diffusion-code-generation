def evaluate_and_gate(input_a, input_b):
    truth_table = {
        (False, False): False,
        (False, True): False,
        (True, False): False,
        (True, True): True,
    }
    if not isinstance(input_a, bool) or not isinstance(input_b, bool):
        raise ValueError("Inputs must be boolean values")
    return truth_table[(input_a, input_b)]

if __name__ == '__main__':
    result = evaluate_and_gate(True, True)
    print(result)