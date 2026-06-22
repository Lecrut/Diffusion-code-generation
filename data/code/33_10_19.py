def triangle_area(base, height):
    return float(base) * float(height) / 2

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    result = triangle_area(base_value, height_value)
    print(result)