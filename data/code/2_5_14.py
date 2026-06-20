import math

def scale_volumes(volumes: list, factor: float) -> list:
    if not isinstance(volumes, list):
        raise TypeError("volumes must be a list")
    if not isinstance(factor, (int, float)):
        raise TypeError("factor must be a number")
    
    scaled = []
    for v in volumes:
        if not isinstance(v, (int, float)):
            raise TypeError(f"Invalid volume value: {v}")
        if v < 0:
            raise ValueError(f"Volume cannot be negative: {v}")
        scaled.append(v * factor)
    return scaled

if __name__ == '__main__':
    initial_volumes = [10.0, 20.5, 30.123]
    scale_factor = 2.5
    
    result = scale_volumes(initial_volumes, scale_factor)
    
    print(result)