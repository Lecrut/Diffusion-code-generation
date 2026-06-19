def is_valid_triangle(sides):
    def has_positive_length(sides):
        return all(side > 0 for side in sides)
    
    def satisfies_triangle_inequality(a, b, c):
        return a + b > c and a + c > b and b + c > a
    
    if len(sides) != 3:
        return False
    if not has_positive_length(sides):
        return False
    sorted_sides = sorted(sides)
    return satisfies_triangle_inequality(*sorted_sides)

if __name__ == '__main__':
    sample_values = [[6, 8, 10], [5, 7, 12], [0, 9, 10], [-4, 5, 6], [7, 7, 7], [3, 4, 8]]
    for sides in sample_values:
        print(is_valid_triangle(sides))