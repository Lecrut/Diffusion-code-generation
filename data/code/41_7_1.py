import math

def calculate_rhombus_area(diagonal_one: float, diagonal_two: float) -> float:
    if diagonal_one <= 0 or diagonal_two <= 0:
        raise ValueError("Diagonals must be positive numbers.")
    
    half_first = diagonal_one * 0.5
    half_second = diagonal_two * 0.5
    return (diagonal_one * diagonal_two) * 0.5

if __name__ == '__main__':
    d1 = 10.5
    d2 = 8.2
    area = calculate_rhombus_area(d1, d2)
    print(area)