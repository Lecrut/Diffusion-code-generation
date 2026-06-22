def max_adjacent_pairs(data):
    if not isinstance(data, tuple) or len(data) < 2:
        raise ValueError("Input must be a non-empty tuple with at least two elements.")
    
    return tuple(max(item1, item2) for item1, item2 in zip(data, data[1:]))

if __name__ == '__main__':
    sample_data = (3, 5, 2, 8, 6)
    try:
        result = max_adjacent_pairs(sample_data)
        print(result)
    except ValueError as e:
        print(e)