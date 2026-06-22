def extract_and_sum_digits(s):
    total = 0
    for char in s:
        if '0' <= char <= '9':
            total += int(char)
    return total

if __name__ == '__main__':
    sample_string = "a1b2c3d4e5f6"
    result = extract_and_sum_digits(sample_string)
    print(result)