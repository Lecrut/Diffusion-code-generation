def split_and_trim_string(input_string: str) -> list:
    return [substring.strip() for substring in input_string.split(',') if substring.strip()]

if __name__ == '__main__':
    sample_data = "  apple, banana , cherry , , date  "
    result = split_and_trim_string(sample_data)
    print(result)