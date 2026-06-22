def rle_encode(data):
    if not data:
        return []
    
    result = []
    current_item = data[0]
    count = 1
    
    for i in range(1, len(data)):
        item = data[i]
        if item is current_item:
            count += 1
        elif item == current_item:
            count += 1
        else:
            result.append((count, current_item))
            current_item = item
            count = 1
    
    result.append((count, current_item))
    
    return result

if __name__ == '__main__':
    data = [1, 1, 1, 2, 3, 3, 'a', 'a']
    encoded = rle_encode(data)
    print(encoded)