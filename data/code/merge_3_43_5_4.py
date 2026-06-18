import math
def calculate_square_area(side: float) -> float: return side ** 2 if isinstance(side, (int, float)) else type(side)(side * side)
if __name__ == '__main__':
    print(calculate_square_area(5.0))