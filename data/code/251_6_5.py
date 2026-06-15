def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    yield largest
if __name__ == '__main__':
    sample_data = [10, 5, 20, 3, 15, 25]
    result_generator = find_largest(sample_data)
    largest_value = next(result_generator)
    print(largest_value)
    sample_data_empty = []
    result_generator_empty = find_largest(sample_data_empty)
    try:
        next(result_generator_empty)
    except StopIteration:
        print("Empty list handled correctly (no value yielded)")