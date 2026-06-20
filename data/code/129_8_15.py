def sort_mixed_data(data):
    if not all(isinstance(item, (int, str)) for item in data):
        raise ValueError("All elements must be either integers or strings")
    
    return sorted(map(str, data), key=lambda s: s)

if __name__ == '__main__':
    sample_data = [1, "apple", 3, "banana", 2, "cherry"]
    sorted_data = sort_mixed_data(sample_data)
    print(sorted_data)