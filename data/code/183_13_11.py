def convert_names(names_str):
    return [name.strip() for name in names_str.split('|') if name.strip()]

if __name__ == '__main__':
    sample_names = "Alice| Bob |Charlie||Dave"
    print(convert_names(sample_names))