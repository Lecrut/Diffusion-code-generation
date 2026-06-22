def analyze_adjacent_pairs(data):
    if not data:
        return []
    
    results = []
    for i in range(len(data) - 1):
        current, next_item = data[i], data[i+1]
        if current < next_item:
            results.append('ascending')
        elif current > next_item:
            results.append('descending')
        else:
            results.append('equal')
    
    return results

if __name__ == '__main__':
    sample_list = [1, 3, 2, 5, 4, 6, 7]
    result = analyze_adjacent_pairs(sample_list)
    print(result)