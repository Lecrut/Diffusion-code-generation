def determine_the_largest_number_present_summary():
    numbers = [34, 56, 23, 89, 12, 45]
    largest_number = max(numbers)
    return {
        'largest_number': largest_number,
        'count': len(numbers),
        'average': sum(numbers) / len(numbers)
    }

if __name__ == '__main__':
    result = determine_the_largest_number_present_summary()
    print(result)