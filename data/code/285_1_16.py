def compare_adjacent_elements(data):
    comparisons = []
    for i in range(len(data) - 1):
        if data[i+1] > data[i]:
            comparisons.append('ascending')
        elif data[i+1] < data[i]:
            comparisons.append('descending')
        else:
            comparisons.append('equal')
    return comparisons

if __name__ == '__main__':
    sample_list = [5, 3, 4, 2, 8, 6, 7]
    result = compare_adjacent_elements(sample_list)
    print(result)