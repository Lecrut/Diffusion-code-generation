def extract_digits(text):
    digits = []
    for char in text:
        if char.isdigit():
            digits.append(int(char))
    return digits

if __name__ == '__main__':
    sample_text = "Room 101 is on 3rd floor, 2024-05-17"
    result = extract_digits(sample_text)
    print(result)
    sample_unicode = "Section ①: 42 items (②)"
    result_unicode = extract_digits(sample_unicode)
    print(result_unicode)