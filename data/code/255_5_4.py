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
    large_data = range(1000000)
    generator = largest_element_generator(large_data)
    result = None
    for num in generator:
        result = num
        break
    print(result)
    large_data_2 = [5, 12, 3, 99, 4]
    generator_2 = largest_element_generator(large_data_2)
    result_2 = next(generator_2)
    print(result_2)
    empty_data = []
    generator_3 = largest_element_generator(empty_data)
    try:
        next(generator_3)
    except StopIteration:
        pass