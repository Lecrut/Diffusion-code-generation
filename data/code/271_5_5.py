def contains_only_digits_and_spaces(s):
    return s.isdigit() or all((c == ' ' for c in s))
if __name__ == '__main__':
    print(contains_only_digits_and_spaces('12345'))
    print(contains_only_digits_and_spaces('123 45'))
    print(contains_only_digits_and_spaces('abc123'))
    print(contains_only_digits_and_spaces('123abc'))
    print(contains_only_digits_and_spaces(' '))
    print(contains_only_digits_and_spaces(''))