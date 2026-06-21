def filter_negative_and_find_min(values):
    positive_values = [x for x in values if x >= 0]
    return min(positive_values) if positive_values else None

if __name__ == '__main__':
    data1 = [5, 2, -8, 1, -9]
    result1 = filter_negative_and_find_min(data1)
    print(f"Data: {data1}, Minimum (Positive): {result1}")

    data2 = [-10, -5, -20, -1]
    result2 = filter_negative_and_find_min(data2)
    print(f"Data: {data2}, Minimum (Positive): {result2}")

    data3 = [100, 50, 25, 75, 0]
    result3 = filter_negative_and_find_min(data3)
    print(f"Data: {data3}, Minimum (Positive): {result3}")