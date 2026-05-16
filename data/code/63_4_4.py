def first_element_generator(iterable):
    try:
        yield next(iter(iterable))
    except StopIteration:
        pass
if __name__ == '__main__':
    data = [10, 20, 30, 40]
    gen = first_element_generator(data)
    result = next(gen)
    print(result)
    data2 = ["a", "b", "c"]
    gen2 = first_element_generator(data2)
    result2 = next(gen2)
    print(result2)
    data3 = []
    gen3 = first_element_generator(data3)
    try:
        next(gen3)
    except StopIteration:
        print("Empty iterable test passed")