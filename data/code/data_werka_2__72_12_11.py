def find_adjacent_inequalities(data):
    results = []
    for i in range(len(data) - 1):
        if data[i] != data[i + 1]:
            results.append((i, data[i], data[i + 1]))
    return results

if __name__ == '__main__':
    sample_data = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
    output = find_adjacent_inequalities(sample_data)
    print(output)