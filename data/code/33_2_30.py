def remove_spaces(s):
    return ''.join(c for c in s if c != ' ')

if __name__ == '__main__':
    sample_string = "  This is a sample string with   various spaces. \nIt has   multiple lines. "
    print(remove_spaces(sample_string))