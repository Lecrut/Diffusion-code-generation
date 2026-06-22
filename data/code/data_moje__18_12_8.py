def median_index_value(data):
    if not data:
        raise ValueError("List must not be empty")
    n = len(data)
    median_index = n // 2
    pivot = data[median_index]
    less = []
    equal = []
    greater = []
    for item in data:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            greater.append(item)
        else:
            equal.append(item)
    if median_index < len(less):
        return median_index_value(less)
    if median_index < len(less) + len(equal):
        return pivot
    return median_index_value(greater)

if __name__ == '__main__':
    sample = [7, 3, 1, 9, 5, 2, 8]
    result = median_index_value(sample)
    print(result)