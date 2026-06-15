def sum_x_coordinates(data):
    total_x = 0
    for x, y in data:
        total_x += x
    return total_x
if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    result = sum_x_coordinates(sample_data)
    print(result)