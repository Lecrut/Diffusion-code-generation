def run_length_encode(data):
    if not data:
        return
    current = data[0]
    count = 1
    for char in data[1:]:
        if char == current:
            count += 1
        else:
            yield (current, count)
            current = char
            count = 1
    yield (current, count)

def run_length_decode(encoded):
    result = []
    for char, count in encoded:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_data = "AAABBBCCDAA"
    encoded = list(run_length_encode(sample_data))
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)