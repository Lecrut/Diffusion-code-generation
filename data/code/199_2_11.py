AVERAGE_LENGTH_THRESHOLD = 5

def filter_long_names(names_list):
    average_length = sum(len(name) for name in names_list) / len(names_list)
    return [name for name in names_list if len(name) > average_length]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    long_names = filter_long_names(sample_names)
    print("Names longer than average length:", long_names)