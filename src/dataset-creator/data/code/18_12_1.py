def reverse_sequence(seq):
    if not isinstance(seq, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    result = []
    for item in seq:
        if isinstance(item, (list, tuple)) and len(result) > 0:
            reversed_item = reverse_sequence(list(item))
            result.append(reversed_item)
        else:
            result.insert(0, item)
    return result
if __name__ == '__main__':
    sample_data = [1, 'a', ['b', {'c': 2}], (3, 4), True]
    reversed_result = reverse_sequence(sample_data)
    print(reversed_result)