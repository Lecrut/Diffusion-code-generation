def is_larger_than(first_number, second_number):
    if not isinstance(first_number, int) or not isinstance(second_number, int):
        raise ValueError("Both inputs must be integers.")
    return first_number > second_number

if __name__ == '__main__':
    try:
        sample_value1 = 25
        sample_value2 = 10
        result = is_larger_than(sample_value1, sample_value2)
        print(result)
    except ValueError as e:
        print(e)