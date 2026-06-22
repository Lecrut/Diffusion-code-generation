def find_min(values):
    if not values:
        raise ValueError("Cannot find minimum of an empty list")
    minimum = values[0]
    for i in range(1, len(values)):
        if values[i] < minimum:
            minimum = values[i]
    return minimum

if __name__ == '__main__':
    sample_data = [5, 2, 9, 1, 7, 6, 3]
    print(find_min(sample_data))
    print(find_min([100, 50, 200, 15, 30]))
    print(find_min([-5, -2, -10, -1]))