def split_and_trim(input_string):
    parts = input_string.split(',')
    trimmed = [part.strip() for part in parts]
    non_empty = [part for part in trimmed if part]
    return non_empty

if __name__ == '__main__':
    sample = "  hello , world ,  , python  ,  "
    result = split_and_trim(sample)
    print(result)