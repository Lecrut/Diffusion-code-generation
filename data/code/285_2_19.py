def compare_consecutive_elements(tup):
    comparison_dict = {}
    for i in range(len(tup) - 1):
        element_pair = (tup[i], tup[i + 1])
        comparison_status = 'equal' if tup[i] == tup[i + 1] else 'not equal'
        comparison_dict[element_pair] = comparison_status
    return comparison_dict

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    result = compare_consecutive_elements(sample_tuple)
    for pair, status in result.items():
        print(f"Pair {pair}: {status}")