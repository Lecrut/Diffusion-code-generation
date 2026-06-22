MAX_VALUE = 1000

def calculate_triangle_perimeter(a, b, c):
    if not (a + b > c and a + c > b and (b + c > a)):
        raise ValueError('The given sides do not form a valid triangle.')
    return a + b + c
if __name__ == '__main__':
    try:
        perimeter1 = calculate_triangle_perimeter(3, 4, 5)
        print(f'Perimeter of triangle (3, 4, 5): {perimeter1}')
        try:
            perimeter2 = calculate_triangle_perimeter(1, 2, 10)
        except ValueError as e:
            print(e)
        try:
            perimeter3 = calculate_triangle_perimeter(MAX_VALUE - 1, MAX_VALUE - 2, 1)
            print(f'Perimeter of triangle (MAX-1, MAX-2, 1): {perimeter3}')
        except ValueError as e:
            print(e)
    except Exception as e:
        print(f'An error occurred: {e}')