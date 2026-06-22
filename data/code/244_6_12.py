def calculate_area(diag1, diag2):
    return 0.5 * diag1 * diag2

def calculate_area_sum():
    area1 = calculate_area(6, 8)
    area2 = calculate_area(10, 12)
    return area1 + area2

if __name__ == '__main__':
    result = calculate_area_sum()
    print(result)