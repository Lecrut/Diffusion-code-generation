def find_largest(data):
    if not data:
        return None
    
    try:
        largest = max(data, key=lambda x: (isinstance(x[1], str), x[1]))
    except TypeError as e:
        raise ValueError("All items in the list must be tuples with two elements") from e
    
    return largest

if __name__ == '__main__':
    sample_data = [("apple", 5), ("banana", 20), ("cherry", 15)]
    print(find_largest(sample_data))