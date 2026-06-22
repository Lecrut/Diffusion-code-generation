def run_length_encode(values):
    if not values:
        return []
    
    encoded = []
    current_value = values[0]
    count = 1
    
    for i in range(1, len(values)):
        value = values[i]
        if value == current_value:
            count += 1
        else:
            encoded.append((current_value, count))
            current_value = value
            count = 1
    
    encoded.append((current_value, count))
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    result = run_length_encode(sample_data)
    print(result)