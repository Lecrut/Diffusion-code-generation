def get_middle_element(iterable):
    iterator = iter(iterable)
    try:
        middle = next(iterator)
    except StopIteration:
        raise ValueError("Input iterable is empty")
    
    try:
        second = next(iterator)
    except StopIteration:
        return middle
    
    count = 2
    while True:
        try:
            current = next(iterator)
            if count % 2 == 0:
                middle = second
            second = current
            count += 1
        except StopIteration:
            break
    
    return middle

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle_element(sample_list)
    print(result)
    
    sample_tuple = (1, 2, 3, 4)
    result2 = get_middle_element(sample_tuple)
    print(result2)
    
    sample_string = "abcde"
    result3 = get_middle_element(sample_string)
    print(result3)