def determine_the_largest_number_present_summary(input_string):
    numbers = []
    for item in input_string.split(','):
        item = item.strip()
        if item:
            try:
                numbers.append(float(item))
            except ValueError:
                continue
    summary = {
        'count': len(numbers),
        'sum': sum(numbers),
        'min': min(numbers) if numbers else None,
        'max': max(numbers) if numbers else None
    }
    return summary

if __name__ == '__main__':
    test_string_1 = "10,5,22,8"
    print(f"Input: '{test_string_1}', Summary: {determine_the_largest_number_present_summary(test_string_1)}")
    test_string_2 = "3.14,1.618,2.718"
    print(f"Input: '{test_string_2}', Summary: {determine_the_largest_number_present_summary(test_string_2)}")
    test_string_3 = "apple,banana,100,orange"
    print(f"Input: '{test_string_3}', Summary: {determine_the_largest_number_present_summary(test_string_3)}")