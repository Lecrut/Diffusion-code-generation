TRUE_VALUE = 1
FALSE_VALUE = 0

def evaluate_three_input_and_gate(input_a, input_b, input_c):
    if not all(isinstance(x, int) for x in (input_a, input_b, input_c)):
        raise ValueError("Inputs must be integers")
    if not all(x in (TRUE_VALUE, FALSE_VALUE) for x in (input_a, input_b, input_c)):
        raise ValueError("Inputs must be 0 or 1")
    result = input_a & input_b & input_c
    return result

if __name__ == '__main__':
    sample_inputs = (TRUE_VALUE, FALSE_VALUE, TRUE_VALUE)
    computed_output = evaluate_three_input_and_gate(*sample_inputs)
    print(computed_output)