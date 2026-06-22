def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    sides.sort()
    smallest, middle, largest = sides
    if smallest <= 0 or middle <= 0 or largest <= 0:
        return False
    return smallest + middle > largest

if __name__ == '__main__':
    sample_values = [[7, 10, 5], [8, 15, 17], [0, 9, 12], [-3, 6, 9], [4, 4, 4], [3, 3, 6]]
    for sides in sample_values:
        print(is_valid_triangle(sides))