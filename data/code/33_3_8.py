def triangle_area(base, height):
    return base * height / 2.0

if __name__ == '__main__':
    base_val = 10.0
    height_val = 5.0
    result = triangle_area(base_val, height_val)
    print(result)