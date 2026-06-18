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
    print(f"Original List: {sample_list}")
    print("Reversed List:", reverse_sequence(sample_list))
    print("\nOriginal Tuple:", sample_tuple)
    print("Reversed Tuple:", reverse_sequence(sample_tuple))
    print("\nOriginal String:", sample_string)
    print("Reversed String:", reverse_sequence(sample_string))