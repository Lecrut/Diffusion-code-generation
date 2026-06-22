SQUARE_SIDE = 4

def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    sample_side = SQUARE_SIDE
    area = calculate_square_area(sample_side)
    print(f"Side: {sample_side}, Area: {area}")