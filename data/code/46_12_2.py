def calculate_perimeter(a, b, c):
    return a + b + c

if __name__ == '__main__':
    sides = {'side_a': 3.0, 'side_b': 4.0, 'side_c': 5.0}
    perimeter = calculate_perimeter(sides['side_a'], sides['side_b'], sides['side_c'])
    print(perimeter)