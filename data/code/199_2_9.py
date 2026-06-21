def filter_long_names(names):
    total_length = sum(len(name) for name in names)
    average_length = total_length / len(names)
    return [name for name in names if len(name) > average_length]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Dave"]
    long_names = filter_long_names(sample_names)
    print(long_names)