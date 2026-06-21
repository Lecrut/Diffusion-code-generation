def convert_names_to_list(names_str):
    return names_str.strip().split('\n')

if __name__ == '__main__':
    sample_names = "Alice\nBob\nCharlie"
    print(convert_names_to_list(sample_names))