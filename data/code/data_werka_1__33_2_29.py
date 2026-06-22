def remove_spaces(s):
    return ''.join(s.split())

if __name__ == '__main__':
    input_string = "  This is an example string with various spaces.\nIt spans multiple lines. "
    cleaned_string = remove_spaces(input_string)
    print(cleaned_string)