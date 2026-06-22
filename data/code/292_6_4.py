def calculate_perimeter(side_lengths):
    return sum(side_lengths)

if __name__ == '__main__':
    sample_sides = [5, 3, 4, 2]
    perimeter = calculate_perimeter(sample_sides)
    print(perimeter)