def get_middle_element(sequence):
    if not hasattr(sequence, '__len__'):
        raise TypeError("Input must be a sequence with a length.")
    
    seq_len = len(sequence)
    if seq_len == 0:
        raise ValueError("Sequence cannot be empty.")
    
    middle_index = (seq_len - 1) // 2
    
    if isinstance(sequence, str):
        result = sequence[middle_index]
        if seq_len % 2 == 0:
            next_char = sequence[middle_index + 1]
            return (result + next_char) / 2.0
        return result
    elif isinstance(sequence, (list, tuple)):
        if seq_len % 2 == 0:
            middle_val = (sequence[middle_index] + sequence[middle_index + 1]) / 2.0
            return middle_val
        return sequence[middle_index]
    else:
        return sequence[middle_index]

if __name__ == '__main__':
    odd_list = [1, 3, 5]
    even_list = [1, 2, 3, 4]
    odd_string = "abc"
    even_string = "abcd"
    
    print(get_middle_element(odd_list))
    print(get_middle_element(even_list))
    print(get_middle_element(odd_string))
    print(get_middle_element(even_string))