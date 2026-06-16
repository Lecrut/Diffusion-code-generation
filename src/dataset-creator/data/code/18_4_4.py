import sys
def reverse_sequence(seq):
    if not isinstance(seq, (list, tuple)):
        raise TypeError(f"Expected list or tuple, got {type(seq).__name__}")
    try:
        reversed_seq = []
        for item in seq:
            if isinstance(item, (list, tuple)) and len(item) > 0:
                inner_reversed = reverse_sequence(list(item))
                reversed_seq.insert(0, inner_reversed)
            else:
                reversed_seq.insert(0, item)
        return tuple(reversed_seq)
    except RecursionError as e:
        raise RuntimeError("Sequence too deeply nested to process") from e
if __name__ == '__main__':
    sample_data = [1, 2, (3, 4), [[5], 6]]
    try:
        result = reverse_sequence(sample_data)
        print(f"Original: {sample_data}")
        print(f"Reversed: {result}")
        if not isinstance(result, tuple):
            sys.exit(1)
    except Exception as e:
        error_msg = str(e).replace("\n", " ")
        print(f"Error processing input: {error_msg}", file=sys.stderr)
        sys.exit(2)