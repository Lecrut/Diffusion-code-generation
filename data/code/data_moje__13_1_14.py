def fetch_element(data, row, col, fallback=None):
    if 0 <= row < len(data) and 0 <= col < len(data[row]):
        return data[row][col]
    return fallback

if __name__ == '__main__':
    matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    result1 = fetch_element(matrix, 1, 2, "Out of bounds")
    result2 = fetch_element(matrix, 5, 1, -1)
    print(result1)
    print(result2)