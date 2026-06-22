def compare_adjacent_elements(data):
    results = []
    for i in range(len(data) - 1):
        val1, val2 = data[i], data[i+1]
        if val1 < val2:
            result = 'asc'
        elif val1 > val2:
            result = 'desc'
        else:
            result = 'eq'
        results.append((val1, val2, result))
    return results

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    print(compare_adjacent_elements(sample_list))