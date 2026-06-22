def calculate_average_of_pairs(data):
    if not all(isinstance(pair, (list, tuple)) and len(pair) > 0 for pair in data):
        raise ValueError("Input must be a list of non-empty lists/tuples")
    
    total_sum = sum(sum(pair) for pair in data)
    total_count = sum(len(pair) for pair in data)
    
    if total_count == 0:
        return 0
    
    return total_sum / total_count

if __name__ == '__main__':
    sample_data = [
        (1, 2),
        (3, 4, 5),
        (6, 7)
    ]
    average = calculate_average_of_pairs(sample_data)
    print(average)