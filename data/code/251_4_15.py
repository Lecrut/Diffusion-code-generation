def determine_the_largest_number_present_summary():
    sample_values = [34, 56, 23, 89, 12, 78]
    largest_number = max(sample_values)
    return {
        'largest_number': largest_number,
        'sample_values': sample_values
    }

if __name__ == '__main__':
    result = determine_the_largest_number_present_summary()
    print(result['largest_number'])