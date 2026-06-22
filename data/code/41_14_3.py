def compute_area(diagonal_1, diagonal_2):
    return (diagonal_1 * diagonal_2) / 2.0

if __name__ == '__main__':
    d1 = 10.0
    d2 = 15.0
    result = compute_area(d1, d2)
    print(result)