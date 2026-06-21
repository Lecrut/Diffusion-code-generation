def filter_long_names(names):
    long_names = [name for name in names if len(name) > 5]
    return long_names

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Eve"]
    result = filter_long_names(sample_names)
    print(result)