def split_by_comma(input_string):
    return [part.strip() for part in input_string.split(',') if part.strip()]
if __name__ == '__main__':
    sample_input = '  apple, banana ,  cherry ,  ,date  ,  elderberry,  '
    result = split_by_comma(sample_input)
    print(result)