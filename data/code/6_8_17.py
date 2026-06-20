def swap_spaces_for_underscores(text):
    result = []
    for char in text:
        if char == ' ':
            result.append('_')
        else:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "  multiple   spaces  "
    sample3 = "no_spaces_here"
    print(swap_spaces_for_underscores(sample1))
    print(swap_spaces_for_underscores(sample2))
    print(swap_spaces_for_underscores(sample3))