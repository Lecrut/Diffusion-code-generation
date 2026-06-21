def find_middle_element(sequence):
    LENGTH_THRESHOLD = 1
    if len(sequence) == 0:
        raise ValueError("Sequence cannot be empty")
    half_len = len(sequence) // 2
    mid_value = sequence[half_len]
    return mid_value

if __name__ == '__main__':
    sample_data = [40, 80, 120, 160, 200, 240, 280]
    result = find_middle_element(sample_data)
    print(result)