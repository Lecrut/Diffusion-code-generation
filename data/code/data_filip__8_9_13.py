def split_and_trim(s):
    return [part.strip() for part in s.split(',') if part.strip()]

if __name__ == '__main__':
    sample_input = "  hello , world ,  , python ,  test  "
    result = split_and_trim(sample_input)
    print(result)