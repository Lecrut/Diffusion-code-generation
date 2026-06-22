def determine_the_largest_number_present_rank_samples():
    SAMPLE_VALUES = [34, 56, 23, 89, 12, 45]
    sorted_values = sorted(SAMPLE_VALUES, reverse=True)
    return sorted_values

if __name__ == '__main__':
    result = determine_the_largest_number_present_rank_samples()
    print(result)