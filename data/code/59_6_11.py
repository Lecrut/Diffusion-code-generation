def digit_sum(number_string: str) -> int:
    total = 0
    for char in number_string:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample_value = "12345"
    result = digit_sum(sample_value)
    print(result)