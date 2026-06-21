def get_first_element(sequence):
    try:
        return sequence[0]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [7, 8, 9]
    sample_tuple = (10, 11, 12)
    empty_list = []
    empty_tuple = ()
    
    print(get_first_element(sample_list))
    print(get_first_element(sample_tuple))
    print(get_first_element(empty_list))
    print(get_first_element(empty_tuple))