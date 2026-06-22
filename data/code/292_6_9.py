def calculate_perimeter(side_lengths):
    perimeter = sum(side_lengths)
    return perimeter

if __name__ == '__main__':
    sides = [10, 20, 30, 40]
    result = calculate_perimeter(sides)
    print(result)