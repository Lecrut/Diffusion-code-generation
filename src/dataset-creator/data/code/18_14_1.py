def reverse_sequence(seq):
    if isinstance(seq, (list, str)):
        return seq[::-1]
    raise TypeError("Input must be a list or string")
if __name__ == '__main__':
    sample_list = [1, 2, 3, 'a', 'b']
    sample_str = "hello"
    print(f"Original List: {sample_list}")
    print(f"Reversed List: {reverse_sequence(sample_list)}")
    print(f"\nOriginal String: {sample_str}")
    print(f"Reversed String: {reverse_sequence(sample_str)}")
    empty_list = []
    reversed_empty = reverse_sequence(empty_list)
    assert reversed_empty == [], "Empty list handling failed"
    print("\nEdge case verified successfully.")