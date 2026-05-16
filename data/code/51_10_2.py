import sys
def calculate_perimeter(sides):
    return sum(sides)
if __name__ == '__main__':
    sample_sides = [5, 10, 12, 15]
    perimeter = calculate_perimeter(sample_sides)
    print(perimeter)