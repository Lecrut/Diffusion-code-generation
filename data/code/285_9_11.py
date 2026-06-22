def compare_adjacent_elements(data):
    results = []
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            result = 'ascending'
        elif data[i] > data[i + 1]:
            result = 'descending'
        else:
            result = 'equal'
        results.append((data[i], data[i + 1], result))
    return results

if __name__ == '__main__':
    sample_list = [
        'apple',
        'banana',
        'cherry',
        'date'
    ]
    print(compare_adjacent_elements(sample_list))