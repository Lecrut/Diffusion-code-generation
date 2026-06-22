def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))

if __name__ == '__main__':
    area = triangle_area(0, 0, 4, 0, 0, 3)
    print(area)