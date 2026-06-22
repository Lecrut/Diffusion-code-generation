def rectangle_area(width, height):
    result = float(width) * float(height)
    return result

if __name__ == '__main__':
    w = 10
    h = 5.5
    area = rectangle_area(w, h)
    print(area)