def run_length_encode(data):
    if not data:
        return []
    encoded = []
    count = 1
    for index in range(1, len(data)):
        if data[index] == data[index - 1]:
            count += 1
        else:
            encoded.append((data[index - 1], count))
            count = 1
    encoded.append((data[-1], count))
    return encoded

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result = run_length_encode(sample_input)
    print(result)