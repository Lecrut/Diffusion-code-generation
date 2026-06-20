def split_and_clean(s):
    return [part.strip() for part in s.split(',') if part.strip()]

if __name__ == '__main__':
    sample = "  apple , banana,  , cherry ,  date  "
    print(split_and_clean(sample))