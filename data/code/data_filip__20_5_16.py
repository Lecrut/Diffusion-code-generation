def run_length_encode(data):
    if not data:
        return []
    compressed = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = char
            count = 1
    compressed.append((current_char, count))
    return compressed

if __name__ == '__main__':
    sample_list = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd']
    result = run_length_encode(sample_list)
    print(result)