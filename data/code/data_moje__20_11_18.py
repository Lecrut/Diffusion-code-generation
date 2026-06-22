def is_even(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    if isinstance(number, float):
        if number != int(number):
            raise ValueError("Input must be an integer")
        number = int(number)
    return number % 2 == 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2, -2, 4, -4, 3, -3, 10, -10]
    for value in sample_values:
        result = is_even(value)
        print(result)