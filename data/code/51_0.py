import sys
def calculate_perimeter(sides):
    if not sides:
        return 0
    return sum(sides)
if __name__ == '__main__':
    sample_sides = [3, 4, 5, 6]
    if len(sample_sides) < 3:
        print("Error: A polygon must have at least three sides.")
    else:
        perimeter = calculate_perimeter(sample_sides)
        print(f"The side lengths provided are: {sample_sides}")
        print(f"The total perimeter is: {perimeter}")