def replace_spaces_with_underscores(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "no spaces here"
    sample3 = "multiple   spaces   between   words"
    print(replace_spaces_with_underscores(sample1))
    print(replace_spaces_with_underscores(sample2))
    print(replace_spaces_with_underscores(sample3))