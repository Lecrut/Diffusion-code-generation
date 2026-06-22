def sum_of_digits(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

if __name__ == '__main__':
    sample_values = [12345, -9876, 0, 1000000000000000000000]
    for value in sample_values:
        result = sum_of_digits(value)
        print(f"{value}: {result}")