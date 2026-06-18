def reverse_sequence(seq):
    if isinstance(seq, str):
        return seq[::-1]
    elif hasattr(seq, '__reversed__'):
        return list(reversed(seq))
    else:
        raise TypeError("Unsupported sequence type")
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_string = "hello"
    print(f"List reversed: {reverse_sequence(sample_list)}")
    print(f"String reversed: '{reverse_sequence(sample_string)}'")