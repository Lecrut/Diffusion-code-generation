def is_odd(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    return bool(n & 1)

if __name__ == '__main__':
    sample_values = [3, 4, 7, -1, 'a']
    for value in sample_values:
        try:
            result = is_odd(value)
            print(f"is_odd({value}) = {result}")
        except ValueError as e:
            print(e)