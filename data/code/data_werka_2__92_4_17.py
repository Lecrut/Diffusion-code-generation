TRUE_STR = 'True'
FALSE_STR = 'False'

def get_opposite_boolean_string(input_str: str) -> str:
    if input_str == TRUE_STR:
        return FALSE_STR
    if input_str == FALSE_STR:
        return TRUE_STR
    raise ValueError(f"Invalid boolean string: {input_str}")

if __name__ == '__main__':
    print(get_opposite_boolean_string('True'))
    print(get_opposite_boolean_string('False'))