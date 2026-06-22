def check_ends(sequence):
    if not hasattr(sequence, '__len__'):
        raise ValueError("Input must be a sequence")
    if len(sequence) == 0:
        return (None, None)
    first = sequence[0]
    last = sequence[-1]
    return (first, last)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result_list = check_ends(sample_list)
    print(result_list)
    
    sample_string = "hello"
    result_string = check_ends(sample_string)
    print(result_string)
    
    sample_tuple = (10, 20, 30)
    result_tuple = check_ends(sample_tuple)
    print(result_tuple)
    
    sample_empty = []
    result_empty = check_ends(sample_empty)
    print(result_empty)