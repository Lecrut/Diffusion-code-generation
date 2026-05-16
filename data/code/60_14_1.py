def last_element_generator(iterable):
    try:
        it = iter(iterable)
        last_element = None
        for element in it:
            last_element = element
        if last_element is not None:
            yield last_element
    except StopIteration:
        return
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print("List 1 last element:", list(last_element_generator(list1)))
    large_list = list(range(1000000))
    print("Large List last element:", list(last_element_generator(large_list)))
    empty_list = []
    print("Empty List last element:", list(last_element_generator(empty_list)))
    tuple1 = (10, 20, 30)
    print("Tuple 1 last element:", list(last_element_generator(tuple1)))
    large_tuple = tuple(range(5000000))
    print("Large Tuple last element:", list(last_element_generator(large_tuple)))