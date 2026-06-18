import math
from typing import List, Tuple, Optional

def cross_product(o: Tuple[float, float], a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """Calculate the cross product of vectors OA and OB."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def distance_squared(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """Calculate squared Euclidean distance between two points."""

if __name__ == '__main__':
    pass
