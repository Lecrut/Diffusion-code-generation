def swap_first_last(s):
    if len(s) < 2:
        return s
    else:
        return s[-1] + s[1:-1] + s[0]
if __name__ == '__main__':
    sample_string_1 = 'hello'
    sample_string_2 = 'a'
    sample_string_3 = ''
    print(swap_first_last(sample_string_1))
    print(swap_first_last(sample_string_2))
    print(swap_first_last(sample_string_3))