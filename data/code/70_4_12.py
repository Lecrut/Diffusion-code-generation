def first_and_last(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return []
    
    last = first
    for item in iterator:
        last = item
    
    if first == last:
        return [first]
    else:
        return [first, last]

if __name__ == '__main__':
    result = first_and_last([1, 2, 3, 4, 5])
    print(result)
    
    result_empty = first_and_last([])
    print(result_empty)
    
    result_single = first_and_last([42])
    print(result_single)