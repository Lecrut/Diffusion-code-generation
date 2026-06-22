def run_length_encode(data):
    if not data:
        return []
    iterator = iter(data)
    try:
        current_char = next(iterator)
    except StopIteration:
        return []
    count = 1
    result = []
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = char
            count = 1
    result.append((count, current_char))
    return result

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)