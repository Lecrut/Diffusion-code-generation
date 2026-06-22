def extract_digits(text):
    result = []
    for char in text:
        if char.isdigit():
            result.append(char)
    return result

if __name__ == '__main__':
    sample_data = "Hello 123 World! @# $5678 & Test 9"
    print(extract_digits(sample_data))