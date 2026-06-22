def extract_digits(input_string):
    result = []
    for char in input_string:
        if char.isdigit():
            result.append(int(char))
    return result

if __name__ == '__main__':
    sample_text = "abc123DEF45.6!7@8#9"
    digits = extract_digits(sample_text)
    print(digits)