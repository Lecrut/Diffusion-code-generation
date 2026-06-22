def sum_of_digits(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample_string = "a1b2c3d4"
    result = sum_of_digits(sample_string)
    print(result)