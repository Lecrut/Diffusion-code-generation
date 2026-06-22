def compress_run_length(data: list) -> list:
    if not data:
        return []
    compressed = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = data[i]
            count = 1
    compressed.append((current_char, count))
    return compressed

if __name__ == '__main__':
    sample_data = ['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a', 'a', 'a']
    result = compress_run_length(sample_data)
    print(result)