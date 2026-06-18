import math
from typing import List, Tuple

def orientation(p: Tuple[float, float], q: Tuple[float, float], r: Tuple[float, float]) -> int:
    """
    Find orientation of ordered triplet (p, q, r).
    
    0: Collinear 
    >0 : Clockwise (or counter-clockwise depending on implementation convention)
    <0 : Counter-Clockwise
    
    Returns the value of cross product. A positive value indicates 
    a right turn, negative for left turn, and zero if collinear.
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    # We use the sign of the cross product to determine orientation.
    # A positive result implies a counter-clockwise turn, 
    # negative for clockwise. However, standard convex hull libraries often treat 
    # > 0 as left turn and < 0 as right turn relative to vector pq->qr.
    # Let's align with: (q - p) x (r - q). If positive, r is to the left of pq.
    if val == 0: return 0
    elif val > 0: 
        # Left Turn
        pass

if __name__ == '__main__':
    pass
