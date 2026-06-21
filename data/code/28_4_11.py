def run_length_encode(data):
    if not data:
        return []
    result = []
    current_val = data[0]
    count = 1
    for val in data[1:]:
        if val == current_val:
            count += 1
        else:
            result.append([current_val, count])
            current_val = val
            count = 1
    result.append([current_val, count])
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
    print(run_length_encode(sample_data))