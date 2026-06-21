def convert_names_to_list(names_str):
    return [name.strip() for name in names_str.split('\n') if name]

if __name__ == '__main__':
    sample_names = "Alice\nBob\nCharlie\n"
    result = convert_names_to_list(sample_names)
    print(result)