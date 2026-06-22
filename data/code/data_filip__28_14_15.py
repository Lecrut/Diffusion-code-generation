def run_length_encode(sequence):
    result = []
    if not sequence:
        return result

    current_obj = sequence[0]
    current_count = 1

    for item in sequence[1:]:
        if item is current_obj:
            current_count += 1
        else:
            result.append((current_obj, current_count))
            current_obj = item
            current_count = 1
    
    result.append((current_obj, current_count))
    return result

if __name__ == '__main__':
    a = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    res = run_length_encode(a)
    print(res)