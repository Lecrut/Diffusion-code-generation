def extract_and_sum_digits(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample_string = "abc123def45"
    result = extract_and_sum_digits(sample_string)
    print(result)