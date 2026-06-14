def sum_x_coordinates(data):
    total_x = 0
    for x, y in data:
        total_x += x
    return total_x
if __name__ == '__main__':
    sample_data = [(1, 5), (3, 8), (7, 2), (4, 9)]
    result = sum_x_coordinates(sample_data)
    print(result)