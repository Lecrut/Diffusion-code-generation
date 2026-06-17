from typing import Sequence, Tuple
def compute_center_coordinate(sequence: Sequence) -> Tuple[float, float]:
    if not sequence:
        return 0.0, 0.0
    length = len(sequence)
    mid_index_1 = (length - 1) // 2
    mid_index_2 = mid_index_1 + 1 if length % 2 == 0 else None
    x_coord = sequence[mid_index_1] / 2.0
    y_coord = sequence[mid_index_1] * 2.0
    return float(x_coord), float(y_coord)
if __name__ == '__main__':
    sample_sequence: Sequence[int] = [1, 3, 5, 7, 9]
    center_x, center_y = compute_center_coordinate(sample_sequence)
    print(f"Center coordinates for {sample_sequence}: ({center_x}, {center_y})")