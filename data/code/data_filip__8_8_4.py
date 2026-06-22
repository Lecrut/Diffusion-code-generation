def split_and_clean(input_string):
    parts = input_string.split(',')
    return [part.strip() for part in parts if part.strip()]

if __name__ == '__main__':
    sample_input = "apple, banana , ,orange,grape , "
    result = split_and_clean(sample_input)
    print(result)