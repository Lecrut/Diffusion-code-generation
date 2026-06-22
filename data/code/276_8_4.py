def repeat_chars(s, U):
    return ''.join([char * U for char in s])

if __name__ == '__main__':
    result = repeat_chars('hello', 3)
    print(result)