def swap_first_last(s):
    if len(s) < 2:
        return s
    else:
        return s[-1] + s[1:-1] + s[0]

if __name__ == '__main__':
    sample_strings = ["hello", "a", "", "ab", "Python"]
    for string in sample_strings:
        print(swap_first_last(string))