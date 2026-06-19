def second_element_generator(iterable):
    iterator = iter(iterable)
    
    def has_next():
        try:
            next(iterator)
            return True
        except StopIteration:
            return False
    
    if not has_next() or not has_next():
        return
    
    yield next(iterator)

if __name__ == '__main__':
    data1 = [10, 20, 30, 40]
    gen1 = second_element_generator(data1)
    print(list(gen1))
    
    data2 = [5, 15]
    gen2 = second_element_generator(data2)
    print(list(gen2))
    
    data3 = [1]
    gen3 = second_element_generator(data3)
    print(list(gen3))
    
    data4 = []
    gen4 = second_element_generator(data4)
    print(list(gen4))