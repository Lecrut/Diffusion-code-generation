def calculate_perimeter(sides):
    return sum(sides)
if __name__ == '__main__':
    side1 = [3, 4, 5]
    perimeter1 = calculate_perimeter(side1)
    print(f"Perimeter of {side1}: {perimeter1}")
    side2 = [10, 20, 30, 40]
    perimeter2 = calculate_perimeter(side2)
    print(f"Perimeter of {side2}: {perimeter2}")
    side3 = [7]
    perimeter3 = calculate_perimeter(side3)
    print(f"Perimeter of {side3}: {perimeter3}")
    side4 = []
    perimeter4 = calculate_perimeter(side4)
    print(f"Perimeter of {side4}: {perimeter4}")