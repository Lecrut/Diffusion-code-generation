def compare_successors(sequence):
    results = []
    for i in range(len(sequence) - 1):
        current = sequence[i]
        next_item = sequence[i+1]
        if current != next_item:
            results.append((current, next_item))
    return results
if __name__ == '__main__':
    data = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 15},
        {'id': 3, 'value': 15},
        {'id': 4, 'value': 20},
        {'id': 5, 'value': 20}
    ]
    comparison_results = compare_successors(data)
    print(comparison_results)