def replace_spaces_with_underscores(text: str) -> str:
    return text.replace(' ', '_')
if __name__ == '__main__':
    sample_text = 'Hello world this is a test string'
    result = replace_spaces_with_underscores(sample_text)
    print(result)
    another_sample = '   Multiple   spaces   '
    result2 = replace_spaces_with_underscores(another_sample)
    print(result2)
    no_spaces = 'NoSpacesHere'
    result3 = replace_spaces_with_underscores(no_spaces)
    print(result3)
    empty_string = ''
    result4 = replace_spaces_with_underscores(empty_string)
    print(result4)
    single_space = ' '
    result5 = replace_spaces_with_underscores(single_space)
    print(result5)