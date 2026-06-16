def reverse_sequence(sequence):
    if isinstance(sequence, (list, tuple)):
        return sequence[::-1]
    elif isinstance(sequence, str):
        return sequence[::-1]
    else:
        raise TypeError("Unsupported type for reversal")
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "hello"
    reversed_list = reverse_sequence(sample_list)
    print(f"Reversed List: {reversed_list}")
    reversed_tuple = reverse_sequence(sample_tuple)
    print(f"Reversed Tuple: {reversed_tuple}")
    reversed_string = reverse_sequence(sample_string)
    print(f"Reversed String: '{reversed_string}'")