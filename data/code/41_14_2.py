def compute_area(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2.0

if __name__ == '__main__':
    d1 = 10.0
    d2 = 5.0
    result = compute_area(d1, d2)
    print(result)