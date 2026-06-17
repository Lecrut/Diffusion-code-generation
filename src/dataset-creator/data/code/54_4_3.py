from typing import Sequence
def get_center_coordinate(sequence: Sequence) -> tuple[int | float]:
    if not sequence:
        return (0.0,)
    length = len(sequence)
    index = length // 2
    if length % 2 == 1:
        val = float(sequence[index])
        return (val, val)
    else:
        mid_left = sequence[length // 2 - 1]
        mid_right = sequence[length // 2]
        avg_val = (float(mid_left) + float(mid_right)) / 2.0
        return (avg_val, avg_val)
if __name__ == '__main__':
    sample_list = [1, 3, 5]
    result = get_center_coordinate(sample_list)
    print(result)