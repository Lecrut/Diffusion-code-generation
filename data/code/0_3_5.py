def extract_digits(s: str) -> str:
    result = []
    for char in s:
        if '0' <= char <= '9':
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "abc123def456"
    extracted = extract_digits(sample_input)
    print(extracted)