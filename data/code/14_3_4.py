def get_third_element(iterable):
    try:
        return iterable[2]
    except (TypeError, IndexError):
        gen = (item for index, item in enumerate(iterable))
        for index, item in enumerate(gen):
            if index == 2:
                return item
        raise IndexError("Iterable has fewer than 3 elements")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_third_element(sample_list)
    print(result)
    
    sample_tuple = ('a', 'b', 'c', 'd')
    result2 = get_third_element(sample_tuple)
    print(result2)
    
    sample_range = range(100, 200)
    result3 = get_third_element(sample_range)
    print(result3)