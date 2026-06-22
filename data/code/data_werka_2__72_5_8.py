def validate_sequence(seq, name):
    if not hasattr(seq, '__iter__'):
        raise ValueError(f'{name} must be iterable')
    return list(seq)

def compare_values(val_a, val_b):
    if val_a > val_b:
        return 'A > B'
    if val_a < val_b:
        return 'A < B'
    return 'A == B'

def compare_lists(list_a, list_b):
    validated_a = validate_sequence(list_a, 'list_a')
    validated_b = validate_sequence(list_b, 'list_b')
    limit = min(len(validated_a), len(validated_b))
    index = 0
    while index < limit:
        result = compare_values(validated_a[index], validated_b[index])
        yield result
        index += 1

if __name__ == '__main__':
    source_x = [5, 12, 3, 15]
    source_y = [4, 12, 6, 20, 25]
    comparison_results = list(compare_lists(source_x, source_y))
    print(comparison_results)