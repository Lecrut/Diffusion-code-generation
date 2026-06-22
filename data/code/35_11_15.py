import math

def calculate_cube_volume(edge_length: float) -> float:
    if edge_length < 0:
        raise ValueError("Edge length must be non-negative")
    return math.pow(edge_length, 3)

if __name__ == '__main__':
    edge = 5.0
    volume = calculate_cube_volume(edge)
    print(volume)