import math

def calculate_square_area(side: float) -> float:
    return side ** 2

if __name__ == '__main__':
    sample_side = 5.0
    area = calculate_square_area(sample_side)
    print(f"Area of a square with side {sample_side}: {area}")