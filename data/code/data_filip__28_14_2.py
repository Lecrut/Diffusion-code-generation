def run_length_encode(data):
    if not data:
        return []
    
    result = []
    current_item = data[0]
    count = 1
    
    for item in data[1:]:
        if item is current_item:
            count += 1
        else:
            result.append((count, current_item))
            current_item = item
            count = 1
    
    result.append((count, current_item))
    return result

if __name__ == '__main__':
    shared_obj = object()
    sample_data = [
        1, 1, 1, shared_obj, shared_obj, "text", "text", 42, 
        42, 42, 42, shared_obj, 99, 99
    ]
    encoded = run_length_encode(sample_data)
    print(encoded)