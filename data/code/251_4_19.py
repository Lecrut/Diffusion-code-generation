def determine_the_largest_number_present_summary(input_string):
    numbers = []
    for item in input_string.split(','):
        item = item.strip()
        if item:
            try:
                numbers.append(float(item))
            except ValueError:
                continue
    if not numbers:
        return None, None, None
    largest_number = max(numbers)
    smallest_number = min(numbers)
    average_number = sum(numbers) / len(numbers)
    return largest_number, smallest_number, average_number

if __name__ == '__main__':
    test_string_1 = "42,3.14,17,89"
    largest, smallest, average = determine_the_largest_number_present_summary(test_string_1)
    print(f"Input: '{test_string_1}', Largest: {largest}, Smallest: {smallest}, Average: {average}")
    
    test_string_2 = "0.5,-3,7.89,1"
    largest, smallest, average = determine_the_largest_number_present_summary(test_string_2)
    print(f"Input: '{test_string_2}', Largest: {largest}, Smallest: {smallest}, Average: {average}")