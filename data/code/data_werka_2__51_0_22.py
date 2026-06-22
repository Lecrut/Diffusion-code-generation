def calculate_perimeter(sides):
    if not sides:
        return 0
    total = sum(sides)
    return total

if __name__ == '__main__':
    sample_sides = [7, 8, 9]
    print(calculate_perimeter(sample_sides))