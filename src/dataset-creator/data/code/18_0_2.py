def reverse_sequence(sequence):
    if isinstance(sequence, (list, tuple)):
        return sequence[::-1]
    elif isinstance(sequence, str):
        return sequence[::-1]
    else:
        raise TypeError("Unsupported type for reversal.")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "hello"
    result_list = reverse_sequence(sample_list)
    print(f"Reversed List: {result_list}")
    result_tuple = reverse_sequence(sample_tuple)
    print(f"Reversed Tuple: {list(result_tuple)}")
    result_string = reverse_sequence(sample_string)
    print(f"Reversed String: '{result_string}'")