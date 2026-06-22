def find_range(sequence):
    if not sequence:
        raise ValueError('Sequence cannot be empty')
    current_min = float('inf')
    current_max = float('-inf')
    for x in sequence:
        if x < current_min:
            current_min = x
        elif x > current_max:
            current_max = x
    return (current_min, current_max)
if __name__ == '__main__':
    data = [10, 5, 20, 3, 15]
    result = find_range(data)
    print(result)