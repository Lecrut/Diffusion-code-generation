def sum_digits(mixed_string):
    total = 0
    for char in mixed_string:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample_values = [
        "abc123",
        "hello45world67",
        "no_digits_here",
        "9876543210",
        "a1b2c3d4e5"
    ]
    for value in sample_values:
        result = sum_digits(value)
        print(result)