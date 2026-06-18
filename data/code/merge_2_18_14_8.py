def reverse_sequence(seq):
    if isinstance(seq, str):
        return seq[::-1]
    elif isinstance(seq, (list, tuple)):
        return list(reversed(list(seq)))
    else:
        raise TypeError("Unsupported sequence type")
if __name__ == '__main__':
    sample_list = [1, 2, 3, 'a', 'b']
    sample_string = "hello"
    print(f"Original List: {sample_list}")
    reversed_list = reverse_sequence(sample_list)
    print(f"Reversed List: {reversed_list}")
    print(f"\nOriginal String: '{sample_string}'")
    reversed_string = reverse_sequence(sample_string)
    print(f"Reversed String: '{reversed_string}'")
    empty_input = []
    result_empty = reverse_sequence(empty_input)
    print(f"\nEmpty Input Result: {result_empty}")