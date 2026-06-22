def digit_sum(number_str: str) -> int:
    total = 0
    for char in number_str:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample_number = "123456789"
    result = digit_sum(sample_number)
    print(result)