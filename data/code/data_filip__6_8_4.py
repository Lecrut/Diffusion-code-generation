def swap_spaces_for_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "python programming is fun"
    sample3 = "no spaces here"
    sample4 = "  multiple   spaces  "

    print(swap_spaces_for_underscores(sample1))
    print(swap_spaces_for_underscores(sample2))
    print(swap_spaces_for_underscores(sample3))
    print(swap_spaces_for_underscores(sample4))