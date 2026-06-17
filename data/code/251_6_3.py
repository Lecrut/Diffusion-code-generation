def find_largest(data_iterator):
    try:
        first_item = next(data_iterator)
    except StopIteration:
        return None
    largest = first_item
    for number in data_iterator:
        if number > largest:
            largest = number
    return largest
def number_stream_generator(iterable):
    return (n for n in iterable)
if __name__ == '__main__':
    sample_data = [10, 5, 20, 3, 15, 25]
    data_iterator = number_stream_generator(sample_data)
    result = find_largest(data_iterator)
    print(result)
    sample_data_2 = [50, 10, 40, 20, 30]
    data_iterator_2 = number_stream_generator(sample_data_2)
    result_2 = find_largest(data_iterator_2)
    print(result_2)
    sample_data_3 = [7]
    data_iterator_3 = number_stream_generator(sample_data_3)
    result_3 = find_largest(data_iterator_3)
    print(result_3)
    sample_data_4 = []
    data_iterator_4 = number_stream_generator(sample_data_4)
    result_4 = find_largest(data_iterator_4)
    print(result_4)