def sort_by_descending(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All elements in the list must be integers or floats")
    
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_values = [7, 2, 5, 3, 1]
    sorted_values = sort_by_descending(sample_values)
    print(sorted_values)