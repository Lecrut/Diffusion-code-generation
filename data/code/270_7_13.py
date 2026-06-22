def remove_spaces(s):
    return s.translate(str.maketrans('', '', ' '))

if __name__ == '__main__':
    sample_string = "Python is great for automation!"
    result = remove_spaces(sample_string)
    print(result)