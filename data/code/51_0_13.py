MIN_SIDES = 3

def calculate_perimeter(sides):
    if len(sides) < MIN_SIDES:
        return None
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [7, 8, 9, 10]
    perimeter = calculate_perimeter(sample_sides)
    if perimeter is not None:
        print(f"The sides of the polygon are: {sample_sides}")
        print(f"The total perimeter is: {perimeter}")
    else:
        print("Error: A polygon must have at least three sides.")