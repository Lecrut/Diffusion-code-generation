import math
def compare_volumes(vol1: float, vol2: float) -> tuple[float, float, float]:
    if vol1 >= vol2:
        larger = vol1
        smaller = vol2
    else:
        larger = vol2
        smaller = vol1
    difference = abs(vol1 - vol2)
    return larger, smaller, difference
if __name__ == '__main__':
    a = 15.75
    b = 22.31
    larger_v, smaller_v, diff = compare_volumes(a, b)
    print(f"Larger volume: {larger_v}")
    print(f"Smaller volume: {smaller_v}")
    print(f"Difference: {diff}")
    a = 100.0
    b = 99.999
    larger_v, smaller_v, diff = compare_volumes(a, b)
    print(f"Larger volume: {larger_v}")
    print(f"Smaller volume: {smaller_v}")
    print(f"Difference: {diff}")
    a = 5.0
    b = 5.0
    larger_v, smaller_v, diff = compare_volumes(a, b)
    print(f"Larger volume: {larger_v}")
    print(f"Smaller volume: {smaller_v}")
    print(f"Difference: {diff}")