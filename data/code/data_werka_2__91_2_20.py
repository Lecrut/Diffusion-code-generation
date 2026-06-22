BOOLEAN_TRUE = True
BOOLEAN_FALSE = False

def invert_boolean_flag(flag_value):
    return not flag_value

def process_state(flag_value):
    inverted = invert_boolean_flag(flag_value)
    return inverted

if __name__ == '__main__':
    is_active = BOOLEAN_TRUE
    output_result = process_state(is_active)
    print(output_result)
    is_active = BOOLEAN_FALSE
    output_result = process_state(is_active)
    print(output_result)