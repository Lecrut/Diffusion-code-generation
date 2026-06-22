PERIMETER_CONSTANT = 1

def calculate_perimeter(side_lengths):
    return sum(side_lengths) * PERIMETER_CONSTANT

if __name__ == '__main__':
    sample_sides = [5, 3, 4, 2]
    print(calculate_perimeter(sample_sides))