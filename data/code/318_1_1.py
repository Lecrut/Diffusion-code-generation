def compare_adjacent(data):
    differences = []
    for i in range(len(data) - 1):
        diff = data[i+1] - data[i]
        differences.append(diff)
    return differences
if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    result = compare_adjacent(sample_list)
    print(result)