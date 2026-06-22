def check_sequence_ends(sequence):
    if not hasattr(sequence, '__getitem__') or not hasattr(sequence, '__len__'):
        raise ValueError("Input must be a sequence type")
    
    length = len(sequence)
    
    if length == 0:
        return (None, None)
    
    first_item = sequence[0]
    
    if length == 1:
        last_item = first_item
    else:
        last_item = sequence[-1]
    
    return (first_item, last_item)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "hello"
    sample_empty = []
    
    print(check_sequence_ends(sample_list))
    print(check_sequence_ends(sample_tuple))
    print(check_sequence_ends(sample_string))
    print(check_sequence_ends(sample_empty))