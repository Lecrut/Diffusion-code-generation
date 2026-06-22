def calculate_area(diag1, diag2):
    return 0.5 * diag1 * diag2

if __name__ == '__main__':
    area1 = calculate_area(6, 8)
    area2 = calculate_area(10, 12)
    result = area1 + area2
    print(result)