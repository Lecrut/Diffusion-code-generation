def clean_names(names_str):
    name_list = names_str.split(',')
    cleaned_names = [name.strip() for name in name_list]
    return cleaned_names

if __name__ == '__main__':
    sample_input = "Alice, Bob , Charlie ,David"
    result = clean_names(sample_input)
    print(result)