def extract_digits(s: str) -> str:
    result = []
    for char in s:
        if '0' <= char <= '9':
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "abc123xyz456"
    print(extract_digits(sample_string))
    sample_string_2 = "NoDigitsHere!"
    print(extract_digits(sample_string_2))
    sample_string_3 = "7890"
    print(extract_digits(sample_string_3))