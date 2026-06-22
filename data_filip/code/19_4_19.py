def rle_encode(data: list[int]) -> list[list[int]]:
    if not data:
        return []
    
    result = []
    count = 1
    current_value = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_value:
            count += 1
        else:
            result.append([count, current_value])
            current_value = data[i]
            count = 1
    
    result.append([count, current_value])
    return result

if __name__ == '__main__':
    sample_input = [1, 1, 1, 2, 3, 3, 2, 2, 2, 2]
    encoded = rle_encode(sample_input)
    print(encoded)