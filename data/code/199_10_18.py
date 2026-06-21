MAX_NAME_LENGTH = 5

def filter_long_names(names_list):
    return [name for name in names_list if len(name) > MAX_NAME_LENGTH]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "alice", "Bob"]
    long_names = filter_long_names(sample_names)
    print(long_names)