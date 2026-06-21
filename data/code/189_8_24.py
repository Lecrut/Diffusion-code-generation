def remove_elements(predicate, lst):
    return [x for x in lst if not predicate(x)]

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3, 4, 5]
    PREDICATE = lambda x: x % 2 == 0
    
    result = remove_elements(PREDICATE, SAMPLE_LIST)
    print(result)