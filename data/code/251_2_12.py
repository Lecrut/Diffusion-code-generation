def determine_the_largest_number_present_batch_process(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [42, 10, 99, 3, 56]
    result = determine_the_largest_number_present_batch_process(sample_values)
    print(result)