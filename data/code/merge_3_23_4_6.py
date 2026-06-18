import itertools

def compare_generators(seq_a: list, seq_b: list) -> None:
    """
    Yields a string describing the comparison result between corresponding elements of two sequences.

    Args:
        seq_a (list): The first sequence to be compared.
        seq_b (list): The second sequence to be compared against the first.

    Example yields:
        'A is greater' if item_from_seq_a > item_from_seq_b
        'B is smaller'   if item_from_seq_b <  item_from_seq_a
        'Equal'          if item_from_seq_a == item_from_seq_b
    """
    for val_a, val_b in itertools.zip_longest(seq_a, seq_b):
        try:
            comparison = (val_a > val_b) and "A is greater" or \
                         (val_b < val_a) and "B is smaller" or \
                         "Equal"
            print(comparison)
        except TypeError:
            # Handles cases where elements might not be directly comparable without raising an error.
            # In this specific task context, we assume inputs are comparable types as per the description's intent.
            continue

if __name__ == '__main__':
    sample_a = [10, 50, 20, 'apple']
    sample_b = [30, 40, 60, 'banana']

    compare_generators(sample_a, sample_b)