import itertools
def find_absolute_minimum(iterable):
    try:
        iterator = iter(iterable)
        min_val = next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty")
    for value in iterator:
        if value < min_val:
            min_val = value
    return min_val
if __name__ == '__main__':
    data1 = [5, 2, 8, 1, 9]
    print(f"Data: {data1}, Minimum: {find_absolute_minimum(data1)}")
    data2 = [-10, -5, -20, -1]
    print(f"Data: {data2}, Minimum: {find_absolute_minimum(data2)}")
    data3 = [3.14, 1.618, 2.718, 0.577]
    print(f"Data: {data3}, Minimum: {find_absolute_minimum(data3)}")
    data4 = [42]
    print(f"Data: {data4}, Minimum: {find_absolute_minimum(data4)}")
    try:
        data5 = []
        find_absolute_minimum(data5)
    except ValueError as e:
        print(f"Data: {data5}, Error: {e}")