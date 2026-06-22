def determine_the_largest_number_present_summary():
    sample_values = [3, 5, 1, 8, 2, 9, 4]
    largest_number = max(sample_values)
    summary = {
        'largest_number': largest_number,
        'count': len(sample_values),
        'average': sum(sample_values) / len(sample_values)
    }
    return summary

if __name__ == '__main__':
    result = determine_the_largest_number_present_summary()
    print(result)