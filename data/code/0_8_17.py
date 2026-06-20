def extract_digits_and_sum(text):
    total = 0
    for char in text:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample_string = "abc123def456"
    result = extract_digits_and_sum(sample_string)
    print(result)