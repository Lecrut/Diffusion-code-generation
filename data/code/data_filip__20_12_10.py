def run_length_encode(sequence: str) -> dict:
    result = {}
    i = 0
    length = len(sequence)
    while i < length:
        char = sequence[i]
        count = 0
        while i < length and sequence[i] == char:
            count += 1
            i += 1
        if char in result:
            result[char] += count
        else:
            result[char] = count
    return result

if __name__ == '__main__':
    data = "aaabbbcca"
    encoded = run_length_encode(data)
    print(encoded)