def run_length_encode(data):
    if not data:
        return ""
    
    result = []
    count = 1
    length = len(data)
    
    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(data[i - 1])
            count = 1
    
    result.append(str(count))
    result.append(data[length - 1])
    
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAABBBCCD"
    encoded = run_length_encode(sample_string)
    print(encoded)