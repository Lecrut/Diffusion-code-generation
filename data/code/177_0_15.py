def split_string_by_spaces(input_str):
    return input_str.split()

if __name__ == '__main__':
    sample_text = "Split this string by spaces"
    result = split_string_by_spaces(sample_text)
    print(result)