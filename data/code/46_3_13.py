import argparse

def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Side lengths must be positive.')
    if not (a + b > c and a + c > b and (b + c > a)):
        raise ValueError('The given side lengths do not form a valid triangle.')
    return a + b + c
if __name__ == '__main__':
    triangles = {'triangle1': {'sides': (3, 4, 5)}, 'triangle2': {'sides': (6, 8, 10)}, 'triangle3': {'sides': (7, 24, 25)}}
    for name, data in triangles.items():
        try:
            perimeter = calculate_triangle_perimeter(*data['sides'])
            print(f'Perimeter of {name}: {perimeter}')
        except ValueError as e:
            print(f'Error calculating perimeter for {name}: {e}')