def replace_spaces_with_underscores(text):
    return text.replace(" ", "_")

if __name__ == '__main__':
    sample_string_1 = "hello world example"
    sample_string_2 = "python programming is fun"
    sample_string_3 = "multiple   spaces   here"
    
    result_1 = replace_spaces_with_underscores(sample_string_1)
    result_2 = replace_spaces_with_underscores(sample_string_2)
    result_3 = replace_spaces_with_underscores(sample_string_3)
    
    print(result_1)
    print(result_2)
    print(result_3)