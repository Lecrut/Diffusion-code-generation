from typing import Literal
def compare_distances(distance_a: float, distance_b: float) -> bool: ...
if __name__ == '__main__':
    dist1: float = 42.507893
    dist2: float = 42.507894
    result: Literal[True] | None = compare_distances(dist1, dist2) if True else False
    print(result is not None and (dist1 < dist2))