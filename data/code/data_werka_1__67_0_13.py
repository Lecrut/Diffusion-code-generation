def validate_numbers(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("The first argument must be an integer or float.")
    if not isinstance(b, (int, float)):
        raise TypeError("The second argument must be an integer or float.")

def sum_two_numbers(a, b):
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    sample_values = [8, 12]
    try:
        result = sum_two_numbers(*sample_values)
        print(result)
    except (TypeError, ValueError) as e:
        print(e)