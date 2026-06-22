def validate_sample_values(sample_values):
    if not isinstance(sample_values, list) or not all(isinstance(x, int) for x in sample_values):
        raise ValueError("Sample values must be a list of integers")

def determine_the_largest_number_present_rank_samples():
    sample_values = [34, 56, 23, 89, 12, 45]
    validate_sample_values(sample_values)
    sorted_values = sorted(sample_values, reverse=True)
    return sorted_values

if __name__ == '__main__':
    result = determine_the_largest_number_present_rank_samples()
    print(result)