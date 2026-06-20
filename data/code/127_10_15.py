def is_odd(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    return number & 1 == 1

if __name__ == '__main__':
    sample_numbers = [3, 4, -5, 0, 2]
    for num in sample_numbers:
        print(is_odd(num))