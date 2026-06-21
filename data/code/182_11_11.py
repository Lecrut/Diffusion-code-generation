def split_into_chars(input_string):
    if not input_string:
        return []
    return list(input_string)

if __name__ == '__main__':
    sample_string = "Hello World"
    result = split_into_chars(sample_string)
    print(result)