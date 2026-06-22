def determine_the_largest_number_present_batch_process(sample_values):
    if not sample_values:
        return None
    return max(sample_values)

if __name__ == '__main__':
    sample_input = [10, 5, 22, 8, 30]
    result = determine_the_largest_number_present_batch_process(sample_input)
    print(result)