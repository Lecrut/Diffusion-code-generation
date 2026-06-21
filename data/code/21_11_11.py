def run_length_encode(data: list) -> list:
    if not data:
        return []
    
    result = []
    current_val = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_val:
            count += 1
        else:
            result.append((current_val, count))
            current_val = data[i]
            count = 1
            
    result.append((current_val, count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 3, 3, 3, 3]
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)