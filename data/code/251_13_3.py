def determine_the_largest_number_present_rank_samples():
    sample_values = [45, 78, 34, 90, 12, 67]
    sorted_values = sorted(sample_values, reverse=True)
    return sorted_values

if __name__ == '__main__':
    result = determine_the_largest_number_present_rank_samples()
    print(result)