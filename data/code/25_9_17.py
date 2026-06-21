def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    count = 1
    n = len(data)
    
    i = 1
    while i < n:
        if data[i] == data[i - 1]:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(data[i - 1])
            count = 1
        i += 1
    
    if count > 1:
        result.append(str(count))
    result.append(data[n - 1])
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbc"
    encoded = run_length_encode(sample_input)
    print(encoded)