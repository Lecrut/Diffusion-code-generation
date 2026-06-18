from typing import Sequence
def get_center_mark(seq: Sequence) -> int | None:
    if not seq:
        return None
    length = len(seq)
    center_float = (length - 1) / 2.0
    if int(center_float) == center_float:
        return int(center_float)
    return None
if __name__ == '__main__':
    sample_sequences = [
        [],
        ["a"],
        ["a", "b"],
        ["x", "y", "z"],
        range(10),
        list(range(9))
    ]
    for seq in sample_sequences:
        result = get_center_mark(seq)
        print(f"Sequence {seq}: Center mark at index {result}")