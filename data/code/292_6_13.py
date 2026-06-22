def calculate_perimeter(side_lengths):
    perimeter = sum(side_lengths)
    return perimeter

if __name__ == '__main__':
    sides = [7, 5, 6, 3, 4]
    perim = calculate_perimeter(sides)
    print(perim)