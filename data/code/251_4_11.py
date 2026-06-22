def determine_the_largest_number_present_summary():
    sample_values = [3, 5, 2, 8, 1, 9]
    largest_number = max(sample_values)
    return {
        'largest_number': largest_number,
        'sample_values': sample_values
    }

if __name__ == '__main__':
    result = determine_the_largest_number_present_summary()
    print(result)