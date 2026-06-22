def split_and_trim(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return [part.strip() for part in s.split(",") if part.strip()]

if __name__ == '__main__':
    sample_input = "  apple , banana ,  cherry ,  "
    result = split_and_trim(sample_input)
    print(result)