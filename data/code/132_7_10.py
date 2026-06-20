def is_valid_input(s):
    return s.isalpha()
if __name__ == '__main__':
    print(is_valid_input('Hello'))
    print(is_valid_input('123'))
    print(is_valid_input(''))
    print(is_valid_input('Hello123'))