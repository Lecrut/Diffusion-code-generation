def sort_tuple(items):
    if not all(isinstance(item, float) for item in items):
        raise ValueError("All elements must be floating-point numbers")
    
    return tuple(sorted(items))

if __name__ == '__main__':
    sample_data = (3.14, 1.0, 5.5, 2.0, 8.9)
    sorted_data = sort_tuple(sample_data)
    print("Sorted tuple:", sorted_data)