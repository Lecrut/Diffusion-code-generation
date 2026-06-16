def find_adjacent_pairs(data):
    pairs = []
    for i in range(len(data) - 1):
        a = data[i]
        b = data[i+1]
        if abs(a - b) == 1:
            pairs.append((a, b))
    return pairs
if __name__ == '__main__':
    sample_list = [1, 2, 5, 4, 8, 9, 10, 13]
    result = find_adjacent_pairs(sample_list)
    print(result)