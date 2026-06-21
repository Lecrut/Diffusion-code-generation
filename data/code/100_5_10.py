def validate_boolean_inputs(value_one, value_two):
    if type(value_one) is not bool:
        raise ValueError("First input must be a boolean")
    if type(value_two) is not bool:
        raise ValueError("Second input must be a boolean")

def compute_and_gate(first_val, second_val):
    return first_val and second_val

def check_two_input_logic(input_x, input_y):
    validate_boolean_inputs(input_x, input_y)
    result = compute_and_gate(input_x, input_y)
    return result

if __name__ == '__main__':
    a = True
    b = False
    outcome = check_two_input_logic(a, b)
    print(outcome)