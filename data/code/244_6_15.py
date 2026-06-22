def calculate_area_sum(diagonals1, diagonals2):
    length1, width1 = map(float, diagonals1.split())
    length2, width2 = map(float, diagonals2.split())
    area1 = 0.5 * length1 * width1
    area2 = 0.5 * length2 * width2
    return area1 + area2

if __name__ == '__main__':
    sample_diagonals1 = "6 8"
    sample_diagonals2 = "10 12"
    result = calculate_area_sum(sample_diagonals1, sample_diagonals2)
    print(result)