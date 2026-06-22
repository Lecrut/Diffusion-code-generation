def calculate_range(sequence):
    if not sequence:
        return None
    current_min = current_max = sequence[0]
    for x in sequence[1:]:
        if x < current_min:
            current_min = x
        elif x > current_max:
            current_max = x
    return current_max - current_min
if __name__ == '__main__':
    data = [34, 78, 23, 65, 90, 12]
    result = calculate_range(data)
    print(result)