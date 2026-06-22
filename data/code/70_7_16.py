def get_first_and_last(sequence):
    if not hasattr(sequence, '__getitem__') or not hasattr(sequence, '__len__'):
        raise ValueError("Input must be a sequence type")
    
    length = len(sequence)
    
    if length == 0:
        return None, None
    
    first = sequence[0]
    
    if length == 1:
        last = first
    else:
        last = sequence[-1]
    
    return first, last

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "hello"
    sample_empty = []
    sample_single = [42]
    
    print(get_first_and_last(sample_list))
    print(get_first_and_last(sample_tuple))
    print(get_first_and_last(sample_string))
    print(get_first_and_last(sample_empty))
    print(get_first_and_last(sample_single))