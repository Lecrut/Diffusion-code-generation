def get_first_and_last(sequence):
    if not hasattr(sequence, '__getitem__') or not hasattr(sequence, '__len__'):
        raise ValueError("Input must be a sequence type")
    
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence must not be empty")
    
    first = sequence[0]
    last = sequence[-1]
    
    return (first, last)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = (100, 200, 300)
    sample_string = "hello"
    
    print(get_first_and_last(sample_list))
    print(get_first_and_last(sample_tuple))
    print(get_first_and_last(sample_string))