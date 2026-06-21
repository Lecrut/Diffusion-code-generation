def find_smallest(generator):
    try:
        smallest = next(generator)
    except StopIteration:
        return None
    
    for number in generator:
        if number < smallest:
            smallest = number
    
    return smallest

if __name__ == '__main__':
    data_generator = (10, 5, 2, 8, 1).__iter__()
    result = find_smallest(data_generator)
    print(result)