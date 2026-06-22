def run_length_encode(data):
    if not data:
        return {}
    result = {}
    current = data[0]
    count = 1
    for item in data[1:]:
        if item == current:
            count += 1
        else:
            result[current] = count
            current = item
            count = 1
    result[current] = count
    return result

if __name__ == '__main__':
    sample = (1, 1, 2, 2, 2, 3, 1)
    print(run_length_encode(sample))