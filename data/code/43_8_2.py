def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    sample_sides = [5, 10, 3]
    
    print("Square Area Calculations")
    print("-" * 20)
    
    for side in sample_sides:
        area = calculate_square_area(side)
        print(f"Side length: {side}")
        print(f"Area: {area}\n")