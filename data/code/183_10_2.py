def strip_names(name_string):
    return [name.strip() for name in name_string.split(',')]

if __name__ == '__main__':
    sample_input = "Alice, Bob , Charlie ,David"
    print(strip_names(sample_input))