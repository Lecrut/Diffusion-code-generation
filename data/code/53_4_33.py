def square_area(side):
    return side * side

if __name__ == '__main__':
    sample_values = {'small': 2, 'medium': 4, 'large': 6}
    for description, side in sample_values.items():
        print(f"The area of the {description} square is: {square_area(side)}")