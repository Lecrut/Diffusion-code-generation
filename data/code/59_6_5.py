def digit_sum(number_str):
    total = 0
    for char in number_str:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    test_value = "12345"
    result = digit_sum(test_value)
    print(result)