def run_length_encode(strings):
    if not strings:
        return []
    
    encoded = []
    current = strings[0]
    count = 1
    
    for i in range(1, len(strings)):
        if strings[i] == current:
            count += 1
        else:
            encoded.append((current, count))
            current = strings[i]
            count = 1
    
    encoded.append((current, count))
    return encoded

if __name__ == '__main__':
    sample = ["a", "a", "b", "c", "c", "c", "d", "d", "a"]
    result = run_length_encode(sample)
    print(result)