def compare_adjacent(data):
    differences = []
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        differences.append(diff)
    return differences
if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    result = compare_adjacent(sample_list)
    print(result)