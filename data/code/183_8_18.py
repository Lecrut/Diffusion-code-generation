def split_names(names_string):
    return names_string.split(' and ')

if __name__ == '__main__':
    sample_names = "Alice and Bob and Charlie"
    print(split_names(sample_names))