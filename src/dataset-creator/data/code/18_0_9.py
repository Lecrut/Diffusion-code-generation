def reverse_sequence(sequence):
    if isinstance(sequence, (list, tuple)):
        return sequence[::-1]
    elif isinstance(sequence, str):
        return sequence[::-1]
    else:
        raise TypeError("Unsupported type for reversal.")
if __name__ == '__main__':
    sample_list = [1, 2, 3, 'a', 'b']
    sample_tuple = (5, 6, 7)
    sample_string = "Hello World"
    print(f"Original List: {sample_list}")
    print("Reversed List:", reverse_sequence(sample_list))
    print("\nOriginal Tuple:", sample_tuple)
    reversed_tuple_result = reverse_sequence(list(sample_tuple))
    print("Reversed Tuple (as list):", reversed_tuple_result)
    print("\nOriginal String:", sample_string)
    print("Reversed String:", reverse_sequence(sample_string))