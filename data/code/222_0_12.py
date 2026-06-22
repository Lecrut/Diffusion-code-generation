def find_smallest_element(values):
    return min(values)

if __name__ == '__main__':
    data_points = [8, 34, -15, 0, 7]
    smallest_value = find_smallest_element(data_points)
    print(smallest_value)