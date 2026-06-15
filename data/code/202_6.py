def find_largest(data):
    if not data:
        return
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    yield largest
if __name__ == '__main__':
    sample_list = [15, 8, 42, 3, 99, 22]
    result_generator = find_largest(sample_list)
    largest_number = None
    for number in result_generator:
        largest_number = number
    print(largest_number)