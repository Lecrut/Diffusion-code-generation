def split_names(name_string):
    names = []
    for name in name_string.split('and'):
        if name.strip():
            names.extend(name.split())
    return [name.strip() for name in names]

if __name__ == '__main__':
    sample_input = "Alice and Bob and Charlie"
    result = split_names(sample_input)
    print(result)