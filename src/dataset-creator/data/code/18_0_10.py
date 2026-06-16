def reverse_sequence(seq):
    if isinstance(seq, (list, tuple)):
        return seq[::-1]
    elif isinstance(seq, str):
        return seq[::-1]
    else:
        raise TypeError("Unsupported sequence type")
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "hello"
    print(f"Original List: {sample_list}")
    print(f"Reversed List: {reverse_sequence(sample_list)}")
    print(f"\nOriginal Tuple: {sample_tuple}")
    print(f"Reversed Tuple: {reverse_sequence(sample_tuple)}")
    print(f"\nOriginal String: '{sample_string}'")
    print(f"Reversed String: '{reverse_sequence(sample_string)}'")