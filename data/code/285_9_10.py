def compare_adjacent_elements(data):
    results = []
    for i in range(len(data) - 1):
        val1, val2 = data[i], data[i+1]
        if val1 < val2:
            results.append((val1, val2, 'ascending'))
        elif val1 > val2:
            results.append((val1, val2, 'descending'))
        else:
            results.append((val1, val2, 'equal'))
    return results

if __name__ == '__main__':
    sample_list = [
        'apple',
        'banana',
        'cherry',
        'date'
    ]
    print("Comparing adjacent strings:")
    comparison_results = compare_adjacent_elements(sample_list)
    for result in comparison_results:
        print(result)