def filter_names_by_length(names):
    if not names:
        return []
    
    total_length = sum(len(name) for name in names)
    average_length = total_length / len(names)
    
    longer_than_average = [name for name in names if len(name) > average_length]
    return longer_than_average

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Dave"]
    result = filter_names_by_length(sample_names)
    print(result)