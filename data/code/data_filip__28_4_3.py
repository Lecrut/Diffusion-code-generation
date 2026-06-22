def run_length_encode(data):
    if not data:
        return []
    result = []
    current_val = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_val:
            count += 1
        else:
            result.append((current_val, count))
            current_val = data[i]
            count = 1
    result.append((current_val, count))
    return result

if __name__ == '__main__':
    input_list = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    print(run_length_encode(input_list))