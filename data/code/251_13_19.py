def validate_sample_values(sample_values):
    if not all(isinstance(x, int) for x in sample_values):
        raise ValueError("All values must be integers.")
    if len(sample_values) < 2:
        raise ValueError("At least two values are required.")

def determine_the_largest_number_present_rank_samples():
    sample_values = [34, 56, 23, 89, 12, 78]
    validate_sample_values(sample_values)
    sorted_values = sorted(sample_values, reverse=True)
    return sorted_values

if __name__ == '__main__':
    result = determine_the_largest_number_present_rank_samples()
    print(result)