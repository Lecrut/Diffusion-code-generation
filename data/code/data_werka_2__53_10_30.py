import math

def calculate_side_length(diagonal: float) -> float:
    return diagonal / math.sqrt(2)

if __name__ == '__main__':
    diagonal_length = 10.0
    side_length = calculate_side_length(diagonal_length)
    print(side_length)