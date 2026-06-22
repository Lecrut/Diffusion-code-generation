SPACE = ' '

def remove_spaces(s):
    return ''.join(c for c in s if c != SPACE)

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test."
    print(remove_spaces(sample_string))