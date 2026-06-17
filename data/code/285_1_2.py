def find_adjacent_greater_pairs(data):
    pairs = []
    for i in range(len(data) - 1):
        if data[i+1] > data[i]:
            pairs.append((data[i], data[i+1]))
    return pairs
if __name__ == '__main__':
    sample_list = [1, 3, 2, 5, 4, 6, 3]
    result = find_adjacent_greater_pairs(sample_list)
    print(result)