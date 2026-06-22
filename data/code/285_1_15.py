ORDER_ASCENDING = 'ascending'
ORDER_DESCENDING = 'descending'
ORDER_EQUAL = 'equal'

def classify_adjacent_pairs(data):
    comparisons = []
    for i in range(len(data) - 1):
        if data[i] < data[i+1]:
            comparisons.append((data[i], data[i+1], ORDER_ASCENDING))
        elif data[i] > data[i+1]:
            comparisons.append((data[i], data[i+1], ORDER_DESCENDING))
        else:
            comparisons.append((data[i], data[i+1], ORDER_EQUAL))
    return comparisons

if __name__ == '__main__':
    sample_list = [1, 3, 2, 5, 4, 6, 7]
    result = classify_adjacent_pairs(sample_list)
    print(result)