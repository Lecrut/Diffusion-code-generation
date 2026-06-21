def run_length_encode(data):
    if not data:
        return []
    
    encoded = []
    current_item = data[0]
    count = 1
    
    for item in data[1:]:
        if item is current_item:
            count += 1
        else:
            encoded.append((current_item, count))
            current_item = item
            count = 1
    encoded.append((current_item, count))
    
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    result = run_length_encode(sample_data)
    print(result)