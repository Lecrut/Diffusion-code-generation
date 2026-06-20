def find_inequality_indices(data):
    for i in range(len(data) - 1):
        if data[i] != data[i + 1]:
            yield i, data[i], data[i + 1]

if __name__ == '__main__':
    sample_data = [1, "apple", [2, 3], {"a": 4}, 5.5]
    for index, value1, value2 in find_inequality_indices(sample_data):
        print(f"Index {index}: {value1} != {value2}")