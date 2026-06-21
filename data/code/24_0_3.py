def rle_compress(data: str) -> str:
    if not data:
        return ""
    
    result = []
    count = 1
    length = len(data)
    
    for i in range(length):
        if i + 1 < length and data[i] == data[i + 1]:
            count += 1
        else:
            result.append(f"{data[i]}{count}")
            count = 1
            
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbcccaadddd"
    compressed_output = rle_compress(sample_input)
    print(compressed_output)