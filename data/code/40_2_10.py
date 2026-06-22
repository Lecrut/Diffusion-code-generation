from typing import Tuple

def calculate_surface_area(length: float, width: float, height: float) -> float:
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    l_val = 5.0
    w_val = 3.0
    h_val = 4.0
    result = calculate_surface_area(l_val, w_val, h_val)
    print(result)