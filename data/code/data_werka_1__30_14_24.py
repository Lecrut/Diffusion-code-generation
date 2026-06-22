def swap_first_last(s):
    if len(s) < 2:
        return s
    return s[-1] + s[1:-1] + s[0]

if __name__ == '__main__':
    sample_values = ["hello", "a", "", "ab", "Python"]
    for value in sample_values:
        print(swap_first_last(value))