def get_first_and_last(sequence):
    if not hasattr(sequence, '__len__'):
        raise ValueError("Input must be a sequence with length.")
    if len(sequence) == 0:
        raise ValueError("Sequence must not be empty.")
    first = sequence[0]
    last = sequence[-1]
    return first, last

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_string = "hello"
    sample_tuple = (1, 2, 3)
    
    print(get_first_and_last(sample_list))
    print(get_first_and_last(sample_string))
    print(get_first_and_last(sample_tuple))