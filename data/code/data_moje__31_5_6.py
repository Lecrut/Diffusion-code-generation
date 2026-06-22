SIDE_LENGTH = 5
AREA = SIDE_LENGTH ** 2

def calculate_square_area(side: int) -> int:
    return side ** 2

if __name__ == '__main__':
    sample_side = 5
    result = calculate_square_area(sample_side)
    print(result)