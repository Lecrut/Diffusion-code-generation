def triangle_area(base, height):
    area = lambda b, h: 0.5 * b * h
    return area(base, height)

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    result = triangle_area(base_value, height_value)
    print(result)