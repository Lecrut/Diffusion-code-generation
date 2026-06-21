def clean_names(names_str):
    names_list = names_str.split(',')
    cleaned_names = [name.strip() for name in names_list]
    return cleaned_names

if __name__ == '__main__':
    sample_input = "Eve, Frank ,Grace"
    result = clean_names(sample_input)
    print(result)