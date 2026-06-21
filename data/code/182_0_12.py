def separate_characters(input_string):
    return '-'.join([char for char in input_string])
if __name__ == '__main__':
    sample = 'hello'
    result = separate_characters(sample)
    print(result)