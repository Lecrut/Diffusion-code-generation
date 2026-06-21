def get_first_element(sequence):
    try:
        return sequence.__getitem__(0)
    except (IndexError, TypeError):
        return None

if __name__ == '__main__':
    sample_list = [13, 14, 15]
    sample_tuple = (16, 17, 18)
    empty_list = []
    empty_tuple = ()
    invalid_input = "not a sequence"
    
    print(get_first_element(sample_list))
    print(get_first_element(sample_tuple))
    print(get_first_element(empty_list))
    print(get_first_element(empty_tuple))
    print(get_first_element(invalid_input))