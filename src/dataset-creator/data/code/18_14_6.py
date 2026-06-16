def reverse_sequence(sequence):
    if isinstance(sequence, str):
        return sequence[::-1]
    elif isinstance(sequence, (list, tuple)):
        return list(reversed(sequence))
    else:
        raise TypeError("Unsupported type")
if __name__ == '__main__':
    sample_list = [1, 2, 3, 'a', 'b']
    sample_string = "hello world"
    print(f"Original List: {sample_list}")
    reversed_list = reverse_sequence(sample_list)
    print(f"Reversed List: {reversed_list}")
    print(f"\nOriginal String: '{sample_string}'")
    reversed_string = reverse_sequence(sample_string)
    print(f"Reversed String: '{reversed_string}'")
    sample_empty = []
    empty_reversed = reverse_sequence(sample_empty)
    print("\nEmpty List Reversed:", empty_reversed)