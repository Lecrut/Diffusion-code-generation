def calculate_range(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    current_min = sequence[0]
    current_max = sequence[0]
    for x in sequence[1:]:
        if x < current_min:
            current_min = x
        elif x > current_max:
            current_max = x
    return current_max - current_min

if __name__ == '__main__':
    data = [10, 5, 20, 3, 15]
    result = calculate_range(data)
    print(result)