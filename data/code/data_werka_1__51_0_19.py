def calculate_perimeter(sides):
    if len(sides) < 3:
        return None
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [7, 8, 9, 10]
    perimeter = calculate_perimeter(sample_sides)
    if perimeter is not None:
        print(f"The side lengths are: {sample_sides}")
        print(f"The total perimeter is: {perimeter}")
    else:
        print("Error: A polygon must have at least three sides.")