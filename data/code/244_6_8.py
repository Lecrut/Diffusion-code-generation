def calculate_area_sum(d1, d2):
    area1 = (d1[0] * d1[1]) / 2
    area2 = (d2[0] * d2[1]) / 2
    return area1 + area2

if __name__ == '__main__':
    diagonals1 = [6, 8]
    diagonals2 = [10, 12]
    result = calculate_area_sum(diagonals1, diagonals2)
    print(result)