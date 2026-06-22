def remove_spaces(s):
    SPACE = ' '
    return ''.join(s.split(SPACE))

if __name__ == '__main__':
    SAMPLE_STRING = "This string has multiple spaces and newlines.\nLet's remove them all."
    print(remove_spaces(SAMPLE_STRING))