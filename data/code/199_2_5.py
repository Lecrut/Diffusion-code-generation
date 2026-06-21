def filter_long_names(names):
    if not names:
        return []
    
    total_length = sum(len(name) for name in names)
    average_length = total_length / len(names)
    
    long_names = [name for name in names if len(name) > average_length]
    return long_names

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    result = filter_long_names(sample_names)
    print(result)