def calculate_perimeter(sides):
    return sum(sides)

if __name__ == '__main__':
    SAMPLE_SIDES = [7, 8, 9]
    perimeter = calculate_perimeter(SAMPLE_SIDES)
    print(perimeter)