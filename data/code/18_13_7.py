def _validate_sequence(sequence):
    if sequence is None:
        raise TypeError("Input must be a sequence")
    return sequence

def retrieve_center_item(items):
    validated_items = _validate_sequence(items)
    if len(validated_items) == 0:
        raise ValueError("Cannot find center of empty sequence")
    index = len(validated_items) // 2
    return validated_items[index]

if __name__ == '__main__':
    odd_sample = [11, 22, 33, 44, 55]
    even_sample = [11, 22, 33, 44]
    result_odd = retrieve_center_item(odd_sample)
    result_even = retrieve_center_item(even_sample)
    print(result_odd)
    print(result_even)