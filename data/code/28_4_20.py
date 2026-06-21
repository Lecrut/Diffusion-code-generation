def run_length_encode(data):
    if not data:
        return []
    result = []
    current = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current:
            count += 1
        else:
            result.append((current, count))
            current = data[i]
            count = 1
    result.append((current, count))
    return result

if __name__ == '__main__':
    sample = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
    print(run_length_encode(sample))