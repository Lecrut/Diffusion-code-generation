def split_and_clean(s):
    return [part.strip() for part in s.split(',') if part.strip()]

if __name__ == '__main__':
    sample_input = "  hello , world ,  , foo , bar  , ,  "
    print(split_and_clean(sample_input))