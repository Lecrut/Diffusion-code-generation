def split_and_trim(s):
    if s is None:
        return []
    return [item.strip() for item in s.split(',') if item.strip()]

if __name__ == '__main__':
    sample_string = "  apple , banana, ,cherry , , date  "
    result = split_and_trim(sample_string)
    print(result)