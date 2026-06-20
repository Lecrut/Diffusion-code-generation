def validate_tuple(input_tuple):
    if not isinstance(input_tuple, tuple) or len(input_tuple) != 3:
        raise ValueError("Input must be a tuple of three boolean values")

def check_mutual_exclusivity(conditions: tuple) -> bool:
    validate_tuple(conditions)
    return sum(conditions) == 1

if __name__ == '__main__':
    sample_conditions = (True, False, False)
    print(check_mutual_exclusivity(sample_conditions))