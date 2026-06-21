def check_ends(sequence):
    if not hasattr(sequence, '__getitem__') or not hasattr(sequence, '__len__'):
        raise ValueError("Input must be a sequence type")
    
    length = len(sequence)
    
    if length == 0:
        return None
    
    if length == 1:
        return (sequence[0], sequence[0])
    
    first = sequence[0]
    last = sequence[-1]
    
    return (first, last)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = (100, 200, 300)
    sample_string = "hello"
    sample_empty = []
    
    print(check_ends(sample_list))
    print(check_ends(sample_tuple))
    print(check_ends(sample_string))
    print(check_ends(sample_empty))