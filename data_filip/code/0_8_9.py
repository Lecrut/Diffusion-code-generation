def sum_digits(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    test_string = "a1b2c3d4"
    result = sum_digits(test_string)
    print(result)