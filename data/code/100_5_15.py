def evaluate_logic_gate(input_a, input_b):
    truth_table = {
        (True, True): True,
        (True, False): False,
        (False, True): False,
        (False, False): False
    }
    if not isinstance(input_a, bool) or not isinstance(input_b, bool):
        raise ValueError("Inputs must be boolean values")
    return truth_table.get((input_a, input_b), False)

if __name__ == '__main__':
    result = evaluate_logic_gate(True, False)
    print(result)