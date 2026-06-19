def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    sample_sides = {
        'small': 3,
        'medium': 5,
        'large': 7
    }
    
    for size, side_length in sample_sides.items():
        area = calculate_square_area(side_length)
        print(f"Size: {size}, Side Length: {side_length}, Area: {area}")