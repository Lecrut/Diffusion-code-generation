def swap_first_last(s):
    if len(s) < 2:
        return s
    return s[-1] + s[1:-1] + s[0]
if __name__ == '__main__':
    print(swap_first_last('hello'))
    print(swap_first_last('a'))
    print(swap_first_last(''))
    print(swap_first_last('ab'))