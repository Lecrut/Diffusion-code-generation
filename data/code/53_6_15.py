def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    sample_sides = {
        'tiny': 1,
        'small': 2,
        'medium': 4,
        'large': 8,
        'huge': 16
    }
    for size, side_length in sample_sides.items():
        area = calculate_square_area(side_length)
        print(f"Size: {size}, Side Length: {side_length}, Area: {area}")