def run_length_encode(strings):
    if not strings:
        return []
    result = []
    current = strings[0]
    count = 1
    for i in range(1, len(strings)):
        if strings[i] == current:
            count += 1
        else:
            result.append((count, current))
            current = strings[i]
            count = 1
    result.append((count, current))
    return result

if __name__ == '__main__':
    sample = ["a", "a", "b", "c", "c", "c", "d", "d", "a", "a", "a"]
    encoded = run_length_encode(sample)
    print(encoded)