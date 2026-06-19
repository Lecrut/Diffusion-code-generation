def square_area(side):
    return side * side

if __name__ == '__main__':
    sample_sides = {
        'tiny': 1,
        'small': 2,
        'medium': 3,
        'large': 4
    }
    for size, side_length in sample_sides.items():
        area = square_area(side_length)
        print(f"Size: {size}, Side Length: {side_length}, Area: {area}")