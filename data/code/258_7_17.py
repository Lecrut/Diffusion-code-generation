def calculate_pairwise_average(nested_tuple):
    if not all(isinstance(t, tuple) and len(t) == 2 for t in nested_tuple):
        raise ValueError("Input must be a list of tuples with exactly two elements each.")
    
    flattened_result = []
    for pair in nested_tuple:
        avg = (sum(pair[0]) + sum(pair[1])) / 2.0
        flattened_result.extend(avg)
    
    return flattened_result

if __name__ == '__main__':
    sample_data = [((1, 2), (3, 4)), ((5, 6), (7, 8))]
    try:
        result = calculate_pairwise_average(sample_data)
        print(result)
    except ValueError as e:
        print(e)