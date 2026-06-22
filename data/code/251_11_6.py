def determine_the_largest_number_present_format_results(numbers):
    largest = max(numbers)
    return f"The largest number present is: {largest}"

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2]
    print(determine_the_largest_number_present_format_results(sample_numbers))