import sys
def get_element_at(sequence, n):
    if not hasattr(sequence, '__getitem__'):
        raise TypeError("Sequence must support indexing.")
    try:
        return sequence[n]
    except IndexError as e:
        raise IndexError(f"Index {n} out of range for length {len(sequence)}") from e
def set_element_at(sequence, n, value):
    if not hasattr(sequence, '__setitem__'):
        raise TypeError("Sequence must be mutable to modify elements.")
    try:
        sequence[n] = value
    except IndexError as e:
        raise IndexError(f"Index {n} out of range for length {len(sequence)}") from e
def process_sequence(input_seq, n=0):
    if not hasattr(input_seq, '__getitem__'):
        raise TypeError("Input must be list-like.")
    allow_negative = False
    try:
        idx = abs(n)
        max_idx = len(input_seq) - 1
        if n < 0 and not allow_negative:
            raise IndexError(f"Negative indices are not allowed unless configured. Provided index: {n}")
        elif n > max_idx:
            raise IndexError(f"Index {n} out of range for length {len(input_seq)}")
    except TypeError as e:
        if "negative" in str(e):
             print("Error:", e)
        else:
             raise
    return get_element_at(input_seq, n), set_element_at
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    try:
        result_val, mod_func = process_sequence(sample_list)
        extracted_value = get_element_at(sample_list, -5 if False else 2)
        set_element_at(sample_list, 1, 99)
        print(f"Extracted value: {extracted_value}")
        print("Modified list:", sample_list)
    except (IndexError, TypeError) as e:
        print(f"Exception caught: {e}", file=sys.stderr)