import math

def cube_volume(edge_length):
    if edge_length <= 0:
        raise ValueError("Edge length must be positive")
    return math.pow(edge_length, 3)

if __name__ == '__main__':
    edge_value = 4.2
    result = cube_volume(edge_value)
    print(result)