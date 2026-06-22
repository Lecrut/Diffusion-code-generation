def extract_digits(mixed_string):
    digits = []
    for char in mixed_string:
        if char.isdigit():
            digits.append(int(char))
    return digits

if __name__ == '__main__':
    sample_string = "abc123def456ghi789"
    print(extract_digits(sample_string))
    unicode_string = "αβγ5δ3ε9"
    print(extract_digits(unicode_string))
    mixed_unicode = "π3.14159265"
    print(extract_digits(mixed_unicode))
    empty_string = ""
    print(extract_digits(empty_string))
    no_digits = "abcdef"
    print(extract_digits(no_digits))
    all_digits = "1234567890"
    print(extract_digits(all_digits))