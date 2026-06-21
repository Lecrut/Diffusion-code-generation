def split_names(names):
    return names.split(' and ')

if __name__ == '__main__':
    sample_names = "Alice and Bob and Charlie"
    print(split_names(sample_names))