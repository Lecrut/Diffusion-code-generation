def split_and_trim_comma_string(s):
    return [part.strip() for part in s.split(',') if part.strip()]

if __name__ == '__main__':
    sample = " apple , banana , , cherry ,  "
    result = split_and_trim_comma_string(sample)
    print(result)