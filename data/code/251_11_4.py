def determine_the_largest_number_present_format_results(sample_results):
    largest_number = max(sample_results)
    return f"The largest number present is: {largest_number}"

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(determine_the_largest_number_present_format_results(sample_values))