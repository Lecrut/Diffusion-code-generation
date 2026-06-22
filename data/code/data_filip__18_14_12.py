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

if __name__ == '__main__':
    sample = "AAABBBCCDAA"
    result = list(run_length_encode(sample))
    print(result)