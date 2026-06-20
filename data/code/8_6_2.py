def split_and_clean(input_string):
    if not input_string:
        return []
    return [part.strip() for part in input_string.split(',') if part.strip()]

if __name__ == '__main__':
    sample_data = "  apple ,banana,,orange,  grape , kiwi  , "
    result = split_and_clean(sample_data)
    print(result)