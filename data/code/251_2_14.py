def determine_the_largest_number_present_batch_process(numbers):
    if not numbers:
        return None
    return max(numbers)

if __name__ == '__main__':
    sample_values = [15, 28, 4, 90, 32]
    result = determine_the_largest_number_present_batch_process(sample_values)
    print(result)