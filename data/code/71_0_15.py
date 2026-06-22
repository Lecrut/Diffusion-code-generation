def find_middle_element(data):
    if not data:
        raise ValueError("Input list must not be empty")
    length = len(data)
    mid_idx = length // 2
    start = mid_idx - (1 if length % 2 == 0 else 0)
    end = mid_idx + 1
    slice_part = data[start:end]
    if length % 2 != 0:
        return slice_part[0]
    return sum(slice_part) / len(slice_part)

if __name__ == '__main__':
    values_odd = [10, 20, 30, 40, 50, 60, 70]
    values_even = [100, 200, 300, 400, 500, 600]
    values_single = [42]
    res1 = find_middle_element(values_odd)
    res2 = find_middle_element(values_even)
    res3 = find_middle_element(values_single)
    print(res1)
    print(res2)
    print(res3)