def find_largest(data_iter):
    try:
        first = next(data_iter)
    except StopIteration:
        return
    largest = first
    for number in data_iter:
        if number > largest:
            largest = number
    yield largest
if __name__ == '__main__':
    sample_data = iter([10, 5, 20, 3, 15, 25])
    result_generator = find_largest(sample_data)
    largest_value = next(result_generator)
    print(largest_value)
    sample_data_2 = iter([-5, -1, -10, -2])
    result_generator_2 = find_largest(sample_data_2)
    largest_value_2 = next(result_generator_2)
    print(largest_value_2)
    sample_data_3 = iter([42])
    result_generator_3 = find_largest(sample_data_3)
    largest_value_3 = next(result_generator_3)
    print(largest_value_3)