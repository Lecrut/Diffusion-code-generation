def is_valid_triangle(sides):
    def are_positive(sides):
        return all(side > 0 for side in sides)

    def triangle_inequality(a, b, c):
        return a + b > c and a + c > b and b + c > a

    if len(sides) != 3:
        return False
    
    sorted_sides = sorted(sides)
    a, b, c = sorted_sides
    
    if not are_positive(sorted_sides):
        return False
    
    return triangle_inequality(a, b, c)

if __name__ == '__main__':
    sample_values = [[6, 8, 10], [5, 5, 5], [2, 3, 4], [0, 2, 3], [-1, 2, 3], [7, 10, 5]]
    for sides in sample_values:
        print(is_valid_triangle(sides))