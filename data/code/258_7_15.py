def calculate_average_of_pairs(nested_tuples):
    AVG_FACTOR = 2.0
    
    results = []
    for pair in nested_tuples:
        if len(pair) == 2 and isinstance(pair[0], tuple) and isinstance(pair[1], tuple):
            avg_value = sum(sum(inner_pair) / AVG_FACTOR for inner_pair in zip(*pair))
            results.append(avg_value)
    
    return results

if __name__ == '__main__':
    sample_data = [((1, 2), (3, 4)), ((5, 6), (7, 8))]
    average_result = calculate_average_of_pairs(sample_data)
    print(average_result)