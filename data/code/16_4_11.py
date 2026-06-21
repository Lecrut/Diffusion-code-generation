def safe_first_element(sequence):
    if len(sequence) == 0:
        raise IndexError("Cannot extract first element from an empty sequence")
    return sequence[0]

if __name__ == '__main__':
    test_list = [10, 20, 30]
    test_tuple = (42, 99)
    empty_sequence = []
    
    print(safe_first_element(test_list))
    print(safe_first_element(test_tuple))
    try:
        print(safe_first_element(empty_sequence))
    except IndexError as e:
        print(e)