def clean_names(names_str):
    return [name.strip() for name in names_str.split(',')]

if __name__ == '__main__':
    sample_input = "Alice, Bob , Charlie ,David"
    print(clean_names(sample_input))