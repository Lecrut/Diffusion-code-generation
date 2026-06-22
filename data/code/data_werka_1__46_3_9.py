import argparse

def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Side lengths must be positive.')
    if not (a + b > c and a + c > b and (b + c > a)):
        raise ValueError('The given side lengths do not form a valid triangle.')
    return a + b + c
if __name__ == '__main__':
    triangles = {'triangle1': {'a': 3, 'b': 4, 'c': 5}, 'triangle2': {'a': 6, 'b': 8, 'c': 10}, 'triangle3': {'a': 7, 'b': 24, 'c': 25}}
    for name, sides in triangles.items():
        try:
            perimeter = calculate_triangle_perimeter(sides['a'], sides['b'], sides['c'])
            print(f'Perimeter of {name}: {perimeter}')
        except ValueError as e:
            print(f'Error calculating perimeter for {name}: {e}')