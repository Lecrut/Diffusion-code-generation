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
            result.append((current_value, count))
            current_value = sequence[i]
            count = 1
    
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1]
    print(run_length_encode(sample))