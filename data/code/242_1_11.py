def triangle_area():
    x1, y1 = 0, 0
    x2, y2 = 4, 0
    x3, y3 = 0, 3
    area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2
    return area

if __name__ == '__main__':
    print(triangle_area())