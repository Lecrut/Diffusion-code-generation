def analyze_adjacent_pairs(data):
    results = []
    for i in range(len(data) - 1):
        if data[i+1] > data[i]:
            results.append("ascending")
        elif data[i+1] < data[i]:
            results.append("descending")
        else:
            results.append("equal")
    return results

if __name__ == '__main__':
    sample_list = [1, 3, 2, 5, 4, 6, 7]
    result = analyze_adjacent_pairs(sample_list)
    print(result)