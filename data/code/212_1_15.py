def find_min_max(sequence):
    if not sequence:
        return None, None
    min_val = max_val = sequence[0]
    for num in sequence[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return min_val, max_val

if __name__ == '__main__':
    sample_sequence = [34, 78, 12, 90, 56]
    print(find_min_max(sample_sequence))