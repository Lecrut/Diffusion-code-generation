def is_negative(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a numeric value")
    return number < 0

if __name__ == '__main__':
    sample_numbers = [-15, 42, 0, -1, 'a']
    for num in sample_numbers:
        try:
            result = is_negative(num)
            print(f"The number {num} is negative: {result}")
        except ValueError as e:
            print(e)