def compute_area(d1, d2):
    area = 0.5 * d1 * d2
    return area

if __name__ == '__main__':
    diagonal1 = 10.0
    diagonal2 = 5.0
    result = compute_area(diagonal1, diagonal2)
    print(result)