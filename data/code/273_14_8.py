def repeat_chars(input_string):
    return ''.join([char * 2 for char in input_string])
if __name__ == '__main__':
    print(repeat_chars('abc'))