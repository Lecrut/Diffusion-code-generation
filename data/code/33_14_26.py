def remove_spaces(input_string):
    return input_string.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '')

if __name__ == '__main__':
    sample_text = "This is a sample text.\nIt contains spaces, tabs\tand newlines."
    result = remove_spaces(sample_text)
    print(result)