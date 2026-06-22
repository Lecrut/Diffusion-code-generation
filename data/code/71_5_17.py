def get_middle_element(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        raise ValueError("Input iterable is empty")
    
    middle = first
    count = 1
    
    for item in iterator:
        if count % 2 == 0:
            middle = item
        count += 1
    
    return middle

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_middle_element(sample_list)
    print(result)