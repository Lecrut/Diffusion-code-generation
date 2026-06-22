def remove_spaces(s):
    return ''.join(c for c in s if c != ' ')

if __name__ == '__main__':
    input_string = "Python 3.8 is great!"
    result = remove_spaces(input_string)
    print(result)