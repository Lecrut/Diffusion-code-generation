def herons_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

if __name__ == '__main__':
    side_x = 10
    side_y = 6
    side_z = 8
    area = herons_area(side_x, side_y, side_z)
    print(area)