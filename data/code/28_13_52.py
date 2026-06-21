def validate_integer(value):
    if not isinstance(value, int):
        raise ValueError(f"Expected an integer, but got {type(value).__name__}")

def is_larger_than(first_number, second_number):
    validate_integer(first_number)
    validate_integer(second_number)
    return first_number > second_number

if __name__ == '__main__':
    sample_value_a = 42
    sample_value_b = 27
    result_of_comparison = is_larger_than(sample_value_a, sample_value_b)
    print(result_of_comparison)