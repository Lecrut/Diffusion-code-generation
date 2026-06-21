HALF = 0.5

def calculate_triangle_area(x, y):
    return abs(HALF * (x * 0 - 0 * y))
if __name__ == '__main__':
    x_sample = 5
    y_sample = 12
    area_result = calculate_triangle_area(x_sample, y_sample)
    print(area_result)