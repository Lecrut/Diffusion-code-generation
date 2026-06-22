def calculate_triangle_area(base, height):
    return float(base * height / 2)

if __name__ == '__main__':
    result = calculate_triangle_area(10, 5)
    print(result)