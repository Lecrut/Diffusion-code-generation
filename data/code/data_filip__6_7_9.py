def replace_spaces_with_underscores(text):
    char_list = list(text)
    processed_chars = [c if c != ' ' else '_' for c in char_list]
    result_string = ''.join(processed_chars)
    return result_string

if __name__ == '__main__':
    sample_input = "the quick brown fox"
    output = replace_spaces_with_underscores(sample_input)
    print(output)