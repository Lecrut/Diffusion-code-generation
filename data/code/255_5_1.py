def largest_element_generator(data):
    if not data:
        return
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    yield largest
if __name__ == '__main__':
    large_dataset = range(1000000)
    generator = largest_element_generator(large_dataset)
    result = next(generator)
    print(result)
    large_dataset_2 = [3, 1, 4, 1, 5, 9, 2]
    generator_2 = largest_element_generator(large_dataset_2)
    result_2 = next(generator_2)
    print(result_2)
    empty_dataset = []
    generator_3 = largest_element_generator(empty_dataset)
    try:
        next(generator_3)
    except StopIteration:
        print("Empty dataset handled correctly (no value yielded).")