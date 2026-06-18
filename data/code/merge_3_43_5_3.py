import math
def calculate_square_area(side_length: float) -> float: return side_length ** 2 if isinstance(side_length, (int | float)) else type("AreaError", (), {"error": "side length must be a number"})()
if __name__ == '__main__':
    assert abs(calculate_square_area(5.0 - calculate_square_area(3))) < 1e-9