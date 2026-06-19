def calculate_perimeter(a, b, c):
    return a + b + c

if __name__ == '__main__':
    side_lengths = {'side1': 7, 'side2': 9, 'side3': 5}
    perimeter = calculate_perimeter(side_lengths['side1'], side_lengths['side2'], side_lengths['side3'])
    print(perimeter)