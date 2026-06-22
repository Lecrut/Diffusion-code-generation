def determine_order(a, b):
    if a < b:
        return "ascending"
    elif a > b:
        return "descending"
    else:
        return "equal"

def analyze_adjacent_pairs(data):
    results = []
    for i in range(len(data) - 1):
        order = determine_order(data[i], data[i+1])
        results.append((data[i], data[i+1], order))
    return results

if __name__ == '__main__':
    sample_list = [1, 3, 2, 5, 4, 6, 7]
    result = analyze_adjacent_pairs(sample_list)
    print(result)