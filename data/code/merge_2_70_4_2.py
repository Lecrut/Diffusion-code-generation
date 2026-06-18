from typing import List, Tuple
def compare_distances(distance_pairs: List[Tuple[float, float]], target1: float, target2: float) -> List[bool]:
    return [d == (target1, target2) for d in distance_pairs]
if __name__ == '__main__':
    distances = [(3.0, 4.0), (5.0, 6.0), (7.0, 8.0)]
    t1, t2 = 5.0, 5.0
    results = compare_distances(distances, t1, t2)
    for i, is_match in enumerate(results):
        print(f"Pair {i+1}: {'Match' if is_match else 'No Match'}")