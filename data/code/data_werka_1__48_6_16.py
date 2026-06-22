import math

def calculate_triangle_sides(a, b):
    if a > b:
        a, b = (b, a)
    c = math.sqrt(a ** 2 + b ** 2)
    return (a, b, c)
if __name__ == '__main__':
    leg1 = 3
    leg2 = 4
    side_lengths = calculate_triangle_sides(leg1, leg2)
    print(side_lengths)