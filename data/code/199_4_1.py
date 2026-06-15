def name_lengths(names):
    result = {}
    for name in names:
        result[name] = len(name)
    return result
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    lengths_dict = name_lengths(sample_names)
    print(lengths_dict)