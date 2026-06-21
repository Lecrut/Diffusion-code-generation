def filter_long_names(names):
    avg_length = sum(len(name) for name in names) / len(names)
    return [name for name in names if len(name) > avg_length]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Dave"]
    long_names = filter_long_names(sample_names)
    print(long_names)