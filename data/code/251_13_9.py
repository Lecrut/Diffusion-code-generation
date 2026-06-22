LARGEST_NUMBER_SAMPLE = [34, 56, 23, 89, 12, 45]

def determine_the_largest_number_present_rank_samples(sample_values):
    return sorted(sample_values, reverse=True)

if __name__ == '__main__':
    result = determine_the_largest_number_present_rank_samples(LARGEST_NUMBER_SAMPLE)
    print(result)