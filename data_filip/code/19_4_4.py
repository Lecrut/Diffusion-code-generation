def run_length_encode(sequence):
    if not sequence:
        return []
    
    result = []
    current_value = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        if sequence[i] == current_value:
            count += 1
        else:
            result.append([count, current_value])
            current_value = sequence[i]
            count = 1
    
    result.append([count, current_value])
    return result

if __name__ == '__main__':
    data = [1, 1, 1, 2, 3, 3, 2, 2, 2, 1]
    encoded = run_length_encode(data)
    print(encoded)