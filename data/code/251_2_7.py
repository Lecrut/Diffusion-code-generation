def determine_the_largest_number_present_batch_process(numbers):
    if not numbers:
        return None
    return max(numbers)

if __name__ == '__main__':
    sample_values = [10, 5, 22, 8, 30]
    result = determine_the_largest_number_present_batch_process(sample_values)
    print(result)