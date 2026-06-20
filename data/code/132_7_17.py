def is_valid_input(s):
    try:
        return s.isalpha() and len(s) > 0
    except TypeError:
        return False
if __name__ == '__main__':
    sample1 = 'Hello'
    sample2 = ''
    sample3 = '123'
    print(is_valid_input(sample1))
    print(is_valid_input(sample2))
    print(is_valid_input(sample3))