def remove_spaces(s):
    return ''.join(c for c in s if c != ' ')

if __name__ == '__main__':
    sample_string = "Python is great!"
    result = remove_spaces(sample_string)
    print(result)