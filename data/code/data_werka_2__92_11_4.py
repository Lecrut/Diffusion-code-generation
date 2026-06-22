TRUE_TO_FALSE = 'False'
FALSE_TO_TRUE = 'True'
VALID_TRUE_STRINGS = frozenset({'true', 't', '1', 'yes', 'y'})
VALID_FALSE_STRINGS = frozenset({'false', 'f', '0', 'no', 'n'})

def flip_boolean_representation(input_str: str) -> str:
    stripped = input_str.strip().lower()
    if stripped in VALID_TRUE_STRINGS:
        return FALSE_TO_TRUE
    if stripped in VALID_FALSE_STRINGS:
        return TRUE_TO_FALSE
    raise ValueError(f"Cannot flip boolean representation: {input_str}")

if __name__ == '__main__':
    print(flip_boolean_representation('True'))
    print(flip_boolean_representation('False'))
    print(flip_boolean_representation('YES'))
    print(flip_boolean_representation('0'))
    print(flip_boolean_representation('1'))
    print(flip_boolean_representation('No'))