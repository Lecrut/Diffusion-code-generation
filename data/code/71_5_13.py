def middle_element_generator(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
        second = next(iterator)
    except StopIteration:
        return
    
    while True:
        yield first
        first, second = second, next(iterator)

if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    gen1 = middle_element_generator(data1)
    print(next(gen1))
    
    data2 = [10, 20, 30, 40, 50, 60]
    gen2 = middle_element_generator(data2)
    print(next(gen2))
    
    data3 = [100]
    gen3 = middle_element_generator(data3)
    print(next(gen3))