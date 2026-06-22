def swap_spaces_for_underscores(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "no spaces here"
    sample3 = "multiple   spaces   between   words"
    print(swap_spaces_for_underscores(sample1))
    print(swap_spaces_for_underscores(sample2))
    print(swap_spaces_for_underscores(sample3))