from math import pow

def compute_volume(edge_length: float) -> float:
    if not isinstance(edge_length, (int, float)):
        raise TypeError("Edge length must be numeric")
    if edge_length <= 0:
        raise ValueError("Edge length must be positive")
    return pow(edge_length, 3)

if __name__ == '__main__':
    side = 10
    vol = compute_volume(side)
    print(vol)