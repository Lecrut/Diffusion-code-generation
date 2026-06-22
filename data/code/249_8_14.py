def find_largest_item(tuples_list):
    if not all(isinstance(item, tuple) and len(item) > 1 for item in tuples_list):
        raise ValueError("All items must be tuples with at least two elements.")
    
    return max(tuples_list, key=lambda x: x[1])

if __name__ == '__main__':
    sample_data = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
    try:
        result = find_largest_item(sample_data)
        print(result)
    except ValueError as e:
        print(e)