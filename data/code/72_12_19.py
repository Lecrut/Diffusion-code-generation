def get_adjacent_changes(sequence):
    differences = []
    index_mapping = {
        'count': 0,
        'first_value': None,
        'second_value': None,
        'indices': []
    }
    count = 0
    current_index = 0
    length = len(sequence)
    while current_index < length - 1:
        first_item = sequence[current_index]
        second_item = sequence[current_index + 1]
        if first_item != second_item:
            differences.append({
                'index': current_index,
                'value_a': first_item,
                'value_b': second_item
            })
            count += 1
        current_index += 1
    index_mapping['count'] = count
    index_mapping['indices'] = differences
    return index_mapping

if __name__ == '__main__':
    sample_input = [10, 10, 20, 20, 30, 30, 30, 40, 40, 50, 50]
    result_data = get_adjacent_changes(sample_input)
    change_indices = [item['index'] for item in result_data['indices']]
    print(change_indices)