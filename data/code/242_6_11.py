def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def circle_area(diameter):
    radius = diameter / 2
    return 3.14159 * (radius ** 2)

if __name__ == '__main__':
    trapezoid = trapezoid_area(6, 8, 4)
    circle = circle_area(5)
    print(trapezoid > circle)