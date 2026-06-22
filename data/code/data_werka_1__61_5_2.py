def fetch_element_by_position(iterable, position):
    return (item for index, item in enumerate(iterable) if index == position)

if __name__ == '__main__':
    large_list = list(range(1000000))
    target_index = 500000
    element_generator = fetch_element_by_position(large_list, target_index)
    result = next(element_generator, None)
    print(result)