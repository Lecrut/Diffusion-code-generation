def get_middle_element(sequence):
    if len(sequence) == 0:
        raise IndexError("Cannot get middle element of an empty sequence")
    mid_index = len(sequence) // 2
    if len(sequence) % 2 == 0:
        return sequence[mid_index]
    else:
        return sequence[mid_index]

if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5]
    print(get_middle_element(test_list))
    
    test_tuple = ('a', 'b', 'c', 'd', 'e', 'f')
    print(get_middle_element(test_tuple))
    
    test_string = "hello"
    print(get_middle_element(test_string))
    
    test_range = list(range(10, 20))
    print(get_middle_element(test_range))
    
    test_empty = []
    try:
        print(get_middle_element(test_empty))
    except IndexError as e:
        print(e)