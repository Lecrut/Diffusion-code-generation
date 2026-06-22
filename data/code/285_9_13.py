def compare_adjacent_elements(strings):
    ORDER_MAP = {1: 'ascending', -1: 'descending', 0: 'equal'}
    results = []
    for i in range(len(strings) - 1):
        comparison_result = (strings[i] > strings[i+1]) - (strings[i] < strings[i+1])
        result_str = ORDER_MAP.get(comparison_result, "Comparison Error")
        results.append((strings[i], strings[i+1], result_str))
    return results

if __name__ == '__main__':
    sample_strings = [
        'apple',
        'banana',
        'cherry',
        'date'
    ]
    print(compare_adjacent_elements(sample_strings))