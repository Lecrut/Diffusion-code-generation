def split_and_clean(input_string):
    return [part.strip() for part in input_string.split(',') if part.strip()]

if __name__ == '__main__':
    sample = " apple , banana , , cherry , date , "
    print(split_and_clean(sample))