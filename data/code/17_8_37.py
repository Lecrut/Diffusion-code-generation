def is_even(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n & 1 == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, -3, -4, 7, 8, None, "string", 3.5]
    for value in sample_values:
        try:
            print(f"is_even({value}) = {is_even(value)}")
        except ValueError as e:
            print(f"is_even({value}) raised an exception: {e}")