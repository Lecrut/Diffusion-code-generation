def get_middle_element(iterable):
    iterator = iter(iterable)
    try:
        middle = next(iterator)
    except StopIteration:
        raise ValueError("Input iterable is empty")
    
    second = next(iterator, None)
    if second is None:
        return middle
    
    count = 2
    for item in iterator:
        count += 1
        if count % 2 == 0:
            middle = second
            second = item
        else:
            second = item
            
    return middle

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_middle_element(sample_list)
    print(result)
    
    sample_range = range(10)
    result_range = get_middle_element(sample_range)
    print(result_range)
    
    sample_string = "hello"
    result_string = get_middle_element(sample_string)
    print(result_string)