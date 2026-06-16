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
    print(f"Reversed List: {reverse_sequence(sample_list)}")
    print(f"\nOriginal String: '{sample_string}'")
    print(f"Reversed String: '{reverse_sequence(sample_string)}'")