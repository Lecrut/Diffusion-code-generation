def compute_area(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

if __name__ == '__main__':
    d1 = 4.0
    d2 = 6.0
    area = compute_area(d1, d2)
    print(area)