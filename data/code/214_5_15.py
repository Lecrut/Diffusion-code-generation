def find_smallest_positive(iterable):
    positive_values = [x for x in iterable if x > 0]
    return min(positive_values) if positive_values else None

if __name__ == '__main__':
    data1 = [-5, -2, 8, 1, 9, 3]
    print(f"Data: {data1}, Smallest Positive: {find_smallest_positive(data1)}")
    data2 = [-10, -5, -20, -1]
    print(f"Data: {data2}, Smallest Positive: {find_smallest_positive(data2)}")
    data3 = [100, 50, 25, 75]
    print(f"Data: {data3}, Smallest Positive: {find_smallest_positive(data3)}")