def is_number(value):
    return isinstance(value, (int, float))

def check_zero(number):
    if not is_number(number):
        raise TypeError("Input must be an integer or float.")
    return number == 0

if __name__ == '__main__':
    sample_values = [5, 0, -3, 0, 10, "a", 4.5]
    for value in sample_values:
        try:
            result = check_zero(value)
            print(f"Input {value} is zero: {result}")
        except TypeError as e:
            print(e)