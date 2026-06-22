def run_length_encode(sequence):
    if not sequence:
        return []
    encoded = []
    current = sequence[0]
    count = 1
    for item in sequence[1:]:
        if item == current:
            count += 1
        else:
            encoded.append((current, count))
            current = item
            count = 1
    encoded.append((current, count))
    return encoded

if __name__ == '__main__':
    sample = 'AAABBBCCDAA'
    result = run_length_encode(sample)
    print(result)