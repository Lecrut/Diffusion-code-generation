def clean_names(names_str):
    name_list = names_str.split(',')
    cleaned_list = [name.strip() for name in name_list]
    return cleaned_list

if __name__ == '__main__':
    sample_names = "  Alice, Bob , Charlie   "
    result = clean_names(sample_names)
    print(result)