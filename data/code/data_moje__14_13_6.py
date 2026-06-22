def get_third_element(sequence):
    iterator = iter(sequence)
    try:
        next(iterator)
        next(iterator)
        return next(iterator)
    except StopIteration:
        raise IndexError("Sequence has fewer than three elements")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c', 'd')
    sample_string = 'xyzw'
    
    print(get_third_element(sample_list))
    print(get_third_element(sample_tuple))
    print(get_third_element(sample_string))