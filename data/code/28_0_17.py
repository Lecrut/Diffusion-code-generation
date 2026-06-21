def run_length_encode(data):
    if not data:
        return []
    result = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append((data[i - 1], count))
            count = 1
    result.append((data[-1], count))
    return result

if __name__ == '__main__':
    sample_string = "aaabbccccdaaa"
    compressed = run_length_encode(sample_string)
    print(compressed)