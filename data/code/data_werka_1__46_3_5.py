import argparse

def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Side lengths must be positive.')
    if not (a + b > c and a + c > b and (b + c > a)):
        raise ValueError('The given side lengths do not form a valid triangle.')
    return a + b + c
if __name__ == '__main__':
    sample_values = [{'sides': [3, 4, 5], 'expected_perimeter': 12}, {'sides': [7, 8, 9], 'expected_perimeter': 24}, {'sides': [1, 2, 3], 'expected_perimeter': None}]
    for sample in sample_values:
        try:
            a, b, c = sample['sides']
            perimeter = calculate_triangle_perimeter(a, b, c)
            print(f'Perimeter of ({a}, {b}, {c}): {perimeter}')
        except ValueError as e:
            print(f"Error for sides {sample['sides']}: {e}")