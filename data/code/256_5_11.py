def calculate_range(sequence):
    if not sequence:
        return None, None
    current_min = current_max = sequence[0]
    for x in sequence[1:]:
        if x < current_min:
            current_min = x
        elif x > current_max:
            current_max = x
    return current_min, current_max

if __name__ == '__main__':
    data = [34, 78, 12, 56, 90, 23]
    min_val, max_val = calculate_range(data)
    print(f"Minimum: {min_val}, Maximum: {max_val}")