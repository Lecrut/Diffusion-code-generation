def run_length_encode(data):
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
    sample_sequence = "111222333311555555"
    result = run_length_encode(sample_sequence)
    print(result)