def largest_element_generator(data):
    if not data:
        return
    current_max = data[0]
    yield current_max
    for element in data[1:]:
        if element > current_max:
            current_max = element
    yield current_max
if __name__ == '__main__':
    large_dataset = range(1000000)
    generator = largest_element_generator(large_dataset)
    result = next(generator)
    print(result)
    another_dataset = [5, 12, 3, 99, 42]
    generator2 = largest_element_generator(another_dataset)
    result2 = next(generator2)
    print(result2)
    empty_dataset = []
    generator3 = largest_element_generator(empty_dataset)
    try:
        next(generator3)
    except StopIteration:
        pass