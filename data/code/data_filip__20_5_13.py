def run_length_encode(data):
    if not data:
        return []
    encoded = []
    current = data[0]
    count = 1
    for char in data[1:]:
        if char == current:
            count += 1
        else:
            encoded.append((current, count))
            current = char
            count = 1
    encoded.append((current, count))
    return encoded

if __name__ == '__main__':
    sample = ['A', 'A', 'B', 'B', 'B', 'C', 'A', 'A']
    print(run_length_encode(sample))