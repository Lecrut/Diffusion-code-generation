def separate_characters(input_string, delimiter):
    return ''.join([char + delimiter for char in input_string])

if __name__ == '__main__':
    result = separate_characters("hello", ", ")
    print(result)