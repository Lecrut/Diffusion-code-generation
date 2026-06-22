def middle_element_generator(iterable):
    TWO = 2
    ZERO = 0
    ONE = 1
    iterator = iter(iterable)
    
    first = next(iterator, None)
    if first is None:
        return
    
    second = next(iterator, None)
    if second is None:
        yield first
        return
    
    result = first
    
    index = ONE
    for item in iterator:
        index += ONE
        result = item
        
    middle_threshold = index // TWO
    
    if index % TWO == ONE:
        for _ in range(middle_threshold):
            next(iterator, None)
        yield result
    else:
        for _ in range(middle_threshold - ONE):
            next(iterator, None)
        yield result

if __name__ == '__main__':
    odd_list = [11, 22, 33, 44, 55]
    odd_gen = middle_element_generator(odd_list)
    print(list(odd_gen))
    
    even_list = [100, 200, 300, 400]
    even_gen = middle_element_generator(even_list)
    print(list(even_gen))
    
    single_list = [999]
    single_gen = middle_element_generator(single_list)
    print(list(single_gen))
    
    empty_list = []
    empty_gen = middle_element_generator(empty_list)
    print(list(empty_gen))