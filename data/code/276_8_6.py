def repeat_chars(s, U):
    return ''.join([c * U for c in s])

if __name__ == '__main__':
    result = repeat_chars("hello", 3)
    print(result)