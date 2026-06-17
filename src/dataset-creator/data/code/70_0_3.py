from typing import Tuple
def compare_distances(val_a: float, val_b: float) -> Tuple[float, float]:
    if val_a > val_b:
        return val_a, val_a - val_b
    else:
        return val_b, abs(val_b - val_a)
if __name__ == '__main__':
    distance_one = 15.7
    distance_two = 23.4
    larger_distance, difference = compare_distances(distance_one, distance_two)
    print(f"Larger value: {larger_distance}")
    print(f"Difference: {difference}")