def compare_successors(sequence):
    results = []
    for current, next_item in zip(sequence, sequence[1:]):
        if current != next_item:
            results.append((current, next_item))
    return results
if __name__ == '__main__':
    data = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 20},
        {'id': 3, 'value': 10},
        {'id': 4, 'value': 40}
    ]
    comparison_results = compare_successors(data)
    print(comparison_results)