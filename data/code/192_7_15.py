def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def common_elements_generator(iter1, iter2):
    set1 = set()
    for item in iter1:
        if item not in set1:
            set1.add(item)
            if item in iter2:
                yield item

if __name__ == '__main__':
    list_a = [1, 5, 2, 8, 3, 9, 4, 7]
    list_b = [8, 3, 1, 9, 6, 2, 10, 5]
    
    if is_iterable(list_a) and is_iterable(list_b):
        common_gen = common_elements_generator(list_a, list_b)
        print(list(common_gen))
    else:
        print("Invalid input: Both inputs must be iterable objects.")