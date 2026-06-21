def remove_spaces(s):
    return s.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '')

if __name__ == '__main__':
    sample_string = "This is a \tsample string.\nIt contains spaces, tabs,\rand newlines."
    result = remove_spaces(sample_string)
    print(result)