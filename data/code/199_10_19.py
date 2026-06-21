def filter_long_names(names):
    return [name for name in names if len(name) > 5]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
    long_names = filter_long_names(sample_names)
    print(long_names)