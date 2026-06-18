def reverse_sequence(sequence):
    if isinstance(sequence, (list, tuple)):
        return sequence[::-1]
    elif isinstance(sequence, str):
        return sequence[::-1]
    else:
        raise TypeError("Unsupported type for reversal.")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 'a', 'b']
    sample_tuple = (5, 6, 7)
    sample_string = "hello world"
    print("Original List:", sample_list)
    reversed_list = reverse_sequence(sample_list)
    print("Reversed List:", reversed_list)
    print("\nOriginal Tuple:", sample_tuple)
    reversed_tuple = reverse_sequence(sample_tuple)
    print("Reversed Tuple:", reversed_tuple)
    print("\nOriginal String:", sample_string)
    reversed_string = reverse_sequence(sample_string)
    print("Reversed String:", reversed_string)