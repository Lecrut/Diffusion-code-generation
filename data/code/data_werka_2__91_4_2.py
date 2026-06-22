NEGATION_MAP = {True: False, False: True}

def get_negated_boolean(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return NEGATION_MAP[value]

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        result = get_negated_boolean(val)
        print(result)