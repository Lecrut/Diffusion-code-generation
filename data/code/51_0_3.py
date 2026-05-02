import sys
def calculate_perimeter(sides):
    if not isinstance(sides, list) or not all(isinstance(side, (int, float)) and side > 0 for side in sides):
        return None
    return sum(sides)
if __name__ == '__main__':
    sample_sides = [3.0, 4.0, 5.0, 6.0]
    perimeter = calculate_perimeter(sample_sides)
    if perimeter is not None:
        print(f"The sides of the polygon are: {sample_sides}")
        print(f"The total perimeter is: {perimeter}")
    else:
        print("Error: Invalid input provided. Sides must be positive numbers.")