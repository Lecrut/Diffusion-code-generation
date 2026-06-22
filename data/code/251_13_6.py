def determine_the_largest_number_present_rank_samples():
    sample_values = [34, 56, 23, 89, 12, 78]
    if not all(isinstance(x, int) for x in sample_values):
        raise ValueError("All elements in the list must be integers.")
    
    sorted_values = sorted(sample_values, reverse=True)
    return sorted_values

if __name__ == '__main__':
    try:
        result = determine_the_largest_number_present_rank_samples()
        print(result)
    except ValueError as e:
        print(e)