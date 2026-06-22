def find_largest_by_second_element(tuples_list):
    if not all(isinstance(item, tuple) and len(item) >= 2 for item in tuples_list):
        raise ValueError("All items must be tuples with at least two elements")
    
    return max(tuples_list, key=lambda x: x[1])

if __name__ == '__main__':
    sample_data = [(1, 3), (4, 1), (2, 5)]
    try:
        result = find_largest_by_second_element(sample_data)
        print(result)
    except ValueError as e:
        print(e)