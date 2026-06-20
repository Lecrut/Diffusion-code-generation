def split_and_clean_string(s):
    return [item.strip() for item in s.split(',') if item.strip()]

if __name__ == '__main__':
    sample_input = "  apple , banana,,  cherry , , date  "
    result = split_and_clean_string(sample_input)
    print(result)