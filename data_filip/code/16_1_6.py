def compress_list(data):
    if not data:
        return []
    
    compressed = []
    current_value = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_value:
            count += 1
        else:
            compressed.append((current_value, count))
            current_value = data[i]
            count = 1
    
    compressed.append((current_value, count))
    return compressed

if __name__ == '__main__':
    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 5, 6, 6]
    result = compress_list(sample_list)
    print(result)