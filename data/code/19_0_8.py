def compress_rle(data: str) -> str:
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
    sample_input = "aaabbccccd"
    encoded_output = compress_rle(sample_input)
    print(encoded_output)