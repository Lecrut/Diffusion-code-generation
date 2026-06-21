def split_names(names_string):
    return [name.strip() for name in names_string.split('and') if name.strip()]

if __name__ == '__main__':
    sample_input = "Alice and Bob and Charlie"
    print(split_names(sample_input))