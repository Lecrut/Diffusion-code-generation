def compress_string(data):
    if not data:
        return ""
    
    compressed = []
    count = 1
    length = len(data)
    
    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed.append(data[i - 1] + str(count))
            count = 1
    
    compressed.append(data[length - 1] + str(count))
    
    return "".join(compressed)

if __name__ == "__main__":
    sample_input = "aaabbccdddd"
    result = compress_string(sample_input)
    print(result)