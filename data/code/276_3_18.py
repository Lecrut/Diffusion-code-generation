def repeat_characters(s, P):
    if not isinstance(s, str) or not isinstance(P, int):
        raise ValueError('Invalid input: s must be a string and P must be an integer')
    return s * P
if __name__ == '__main__':
    print(repeat_characters('abc', 3))
    print(repeat_characters('hello', 2))