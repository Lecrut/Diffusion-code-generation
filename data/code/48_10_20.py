def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    side_map = {'a': sides[0], 'b': sides[1], 'c': sides[2]}
    for key, value in side_map.items():
        if value <= 0:
            return False
    a, b, c = sorted(sides)
    return a + b > c

if __name__ == '__main__':
    sample_values = [
        [3, 4, 5], 
        [1, 2, 3], 
        [0, 4, 5], 
        [-1, 4, 5], 
        [5, 5, 5], 
        [2, 2, 4],
        [6, 8, 10],
        [7, 10, 5]
    ]
    for sides in sample_values:
        print(is_valid_triangle(sides))