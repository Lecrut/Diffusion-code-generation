def is_even(number: int) -> bool:
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    return number % 2 == 0

if __name__ == '__main__':
    sample_values = [0, 1, -2, 3, -4, 5, -6]
    for value in sample_values:
        print(f"is_even({value}) = {is_even(value)}")