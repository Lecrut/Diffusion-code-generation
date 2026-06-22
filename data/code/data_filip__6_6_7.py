def replace_spaces_with_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_string = "Hello World from Python"
    result = replace_spaces_with_underscores(sample_string)
    print(result)

    sample_string_2 = "NoSpacesHere"
    result_2 = replace_spaces_with_underscores(sample_string_2)
    print(result_2)

    sample_string_3 = "  Leading and trailing  "
    result_3 = replace_spaces_with_underscores(sample_string_3)
    print(result_3)