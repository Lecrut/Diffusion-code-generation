def determine_the_largest_number_present_batch_process(values):
    try:
        numbers = [int(x) for x in values.split()]
        if not numbers:
            raise ValueError("No valid numbers found.")
        return max(numbers)
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    sample_values = "10 5 22 8 30"
    result = determine_the_largest_number_present_batch_process(sample_values)
    print(result)