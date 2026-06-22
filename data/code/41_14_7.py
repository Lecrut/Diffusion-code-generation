def compute_area(diagonal1, diagonal2):
    area = (diagonal1 * diagonal2) / 2.0
    return area

if __name__ == '__main__':
    result = compute_area(10.0, 8.0)
    print(result)