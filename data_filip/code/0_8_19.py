def sum_digits_from_string(mixed_string: str) -> int:
    total = 0
    for char in mixed_string:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample_string = "abc123xyz456"
    result = sum_digits_from_string(sample_string)
    print(result)