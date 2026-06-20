def split_and_clean_string(s):
    return [item.strip() for item in s.split(',') if item.strip()]

if __name__ == '__main__':
    sample = "  apple , banana,  ,cherry,  "
    result = split_and_clean_string(sample)
    print(result)