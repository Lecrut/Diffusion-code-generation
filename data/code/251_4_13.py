def determine_the_largest_number_present_summary():
    sample_values = [34, 56, 23, 89, 12, 45]
    largest_number = max(sample_values)
    summary = {
        'largest_number': largest_number,
        'sample_size': len(sample_values),
        'average': sum(sample_values) / len(sample_values)
    }
    return summary

if __name__ == '__main__':
    result = determine_the_largest_number_present_summary()
    print(result)