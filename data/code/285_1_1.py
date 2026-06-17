def find_greater_adjacent_pairs(data):
    pairs = []
    for i in range(len(data) - 1):
        if data[i] > data[i+1]:
            pairs.append((data[i], data[i+1]))
    return pairs
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3, 9, 4]
    result = find_greater_adjacent_pairs(sample_list)
    print(result)