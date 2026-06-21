import itertools

def run_length_encode(data):
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

def run_length_encode_iterable(data_iter):
    result = []
    try:
        current_char = next(data_iter)
    except StopIteration:
        return result
    count = 1
    for char in data_iter:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

def run_length_encode_iterator_based(data):
    if not data:
        return []
    group_iter = itertools.groupby(data)
    result = []
    for char, group in group_iter:
        count = sum(1 for _ in group)
        result.append((char, count))
    return result

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_result = run_length_encode_iterator_based(sample_string)
    print(encoded_result)