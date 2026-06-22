def run_length_encode(data):
    if not data:
        return {}
    result = {}
    current = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current:
            count += 1
        else:
            result[current] = count
            current = data[i]
            count = 1
    result[current] = count
    return result

if __name__ == '__main__':
    sample_data = ('a', 'a', 'b', 'b', 'b', 'c')
    encoded = run_length_encode(sample_data)
    print(encoded)