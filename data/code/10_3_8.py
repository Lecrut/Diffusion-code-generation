def extract_first_name(name_list):
    return name_list[0]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie"]
    first = extract_first_name(sample_names)
    print(first)