def find_extremes(data):
    if not data:
        return None
    smallest = largest = data[0]
    for value in data:
        if value < smallest:
            smallest = value
        elif value > largest:
            largest = value
    return smallest, largest

if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 77, 5]
    extremes = find_extremes(sample_list)
    print(f"Smallest value: {extremes[0]}")
    print(f"Largest value: {extremes[1]}")