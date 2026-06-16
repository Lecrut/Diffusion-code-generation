def find_adjacent_pairs(data):
    pairs = []
    for i in range(len(data) - 1):
        if abs(data[i] - data[i+1]) == 1:
            pairs.append((data[i], data[i+1]))
    return pairs
if __name__ == '__main__':
    sample_list = [1, 2, 5, 4, 3, 7, 8, 9]
    result = find_adjacent_pairs(sample_list)
    print(result)