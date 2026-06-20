def split_by_comma(s):
    return [part.strip() for part in s.split(',') if part.strip()]

if __name__ == '__main__':
    sample = "  apple , banana ,  , cherry ,  date  "
    result = split_by_comma(sample)
    print(result)