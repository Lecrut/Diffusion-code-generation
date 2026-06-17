def find_min_max(iterable):
    if not iterable:
        raise ValueError("Iterable cannot be empty")
    return min(iterable), max(iterable)
if __name__ == '__main__':
    data1 = (5, 2, 8, 1, 9)
    print(f"Data: {data1}, Min: {find_min_max(data1)}, Max: {find_min_max(data1)}")
    data2 = {100, -50, 300, 10}
    print(f"Data: {data2}, Min: {find_min_max(data2)}, Max: {find_min_max(data2)}")
    data3 = [3.14, 1.618, 2.718]
    print(f"Data: {data3}, Min: {find_min_max(data3)}, Max: {find_min_max(data3)}")
    data4 = (42,)
    print(f"Data: {data4}, Min: {find_min_max(data4)}, Max: {find_min_max(data4)}")
    try:
        empty_data = ()
        find_min_max(empty_data)
    except ValueError as e:
        print(f"Error handling empty iterable: {e}")