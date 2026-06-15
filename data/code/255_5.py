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
    another_dataset = [3, 1, 4, 1, 5, 9, 2]
    generator2 = largest_element_generator(another_dataset)
    result2 = next(generator2)
    print(result2)
    empty_dataset = []
    generator3 = largest_element_generator(empty_dataset)
    try:
        next(generator3)
    except StopIteration:
        pass