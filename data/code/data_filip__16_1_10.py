def run_length_encode(lst):
    if not lst:
        return []
    
    encoded = []
    current_value = lst[0]
    count = 1
    
    for i in range(1, len(lst)):
        if lst[i] == current_value:
            count += 1
        else:
            encoded.append((current_value, count))
            current_value = lst[i]
            count = 1
    
    encoded.append((current_value, count))
    return encoded

if __name__ == '__main__':
    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]
    result = run_length_encode(sample_list)
    print(result)