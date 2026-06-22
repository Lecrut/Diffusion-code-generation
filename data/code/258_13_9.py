def calculate_averages(pair1, pair2):
    return tuple((x + y) / 2 for x, y in zip(pair1, pair2))

if __name__ == '__main__':
    result = calculate_averages((10, 20, 30), (40, 50, 60))
    print(result)