def remove_spaces(s):
    return ''.join(char for char in s if char != ' ')

if __name__ == '__main__':
    sample_string = "This is a sample string with spaces."
    cleaned_string = remove_spaces(sample_string)
    print(cleaned_string)