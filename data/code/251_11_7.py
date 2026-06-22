def determine_the_largest_number_present_format_results(numbers):
    largest_number = max(numbers)
    return f"The largest number present is: {largest_number}"

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2]
    result = determine_the_largest_number_present_format_results(sample_numbers)
    print(result)