def run_length_encode(data: list) -> list:
    if not data:
        return []
    
    result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = data[i]
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    input_list = ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C']
    encoded = run_length_encode(input_list)
    print(encoded)