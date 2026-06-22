if __name__ == '__main__':
    sample_string = 'Hello World! This is a test.'
    result = ''.join(char for char in sample_string if char != ' ')
    print(result)