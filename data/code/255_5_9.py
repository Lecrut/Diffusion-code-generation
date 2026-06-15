def largest_element_generator(iterable):
    try:
        iterator = iter(iterable)
        largest = next(iterator)
    except StopIteration:
        return
    for element in iterator:
        if element > largest:
            largest = element
    yield largest
if __name__ == '__main__':
    data1 = [10, 5, 20, 8, 15]
    gen1 = largest_element_generator(data1)
    result1 = next(gen1)
    print(f"Data: {data1}, Largest element: {result1}")
    data2 = [100, 50, 200, 80, 15]
    gen2 = largest_element_generator(data2)
    result2 = next(gen2)
    print(f"Data: {data2}, Largest element: {result2}")
    data3 = [-5, -1, -10, -8]
    gen3 = largest_element_generator(data3)
    result3 = next(gen3)
    print(f"Data: {data3}, Largest element: {result3}")
    data4 = [42]
    gen4 = largest_element_generator(data4)
    result4 = next(gen4)
    print(f"Data: {data4}, Largest element: {result4}")
    data5 = []
    gen5 = largest_element_generator(data5)
    try:
        next(gen5)
    except StopIteration:
        print(f"Data: {data5}, No largest element found (empty set)")