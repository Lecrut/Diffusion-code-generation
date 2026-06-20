def replace_whitespace_with_underscores(s):
    result = []
    for char in s:
        if char.isspace():
            result.append('_')
        else:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "   Spaces   Everywhere  "
    sample3 = "NoSpacesHere"
    sample4 = "Tab\there\tand\nnewline"
    print(replace_whitespace_with_underscores(sample1))
    print(replace_whitespace_with_underscores(sample2))
    print(replace_whitespace_with_underscores(sample3))
    print(replace_whitespace_with_underscores(sample4))