def compute_area(diagonal1, diagonal2):
    return abs(diagonal1 * diagonal2) / 2

if __name__ == '__main__':
    result = compute_area(10.0, 8.0)
    print(result)