def remove_consecutive_spaces(s):
    return ' '.join(s.split())

if __name__ == '__main__':
    sample_string = "  This   is  a test string. "
    cleaned_string = remove_consecutive_spaces(sample_string)
    print(cleaned_string)