from typing import Union

def cube_volume(edge_length: Union[int, float]) -> float:
    return float(edge_length ** 3)

if __name__ == '__main__':
    result = cube_volume(5)
    print(result)