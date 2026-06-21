def rle_compress(data):
    if not data:
        return ""
    
    result = []
    count = 1
    char = data[0]
    
    for i in range(1, len(data)):
        if data[i] == char:
            count += 1
        else:
            result.append(f"{count}{char}")
            char = data[i]
            count = 1
    
    result.append(f"{count}{char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_text = "AAABBBCCCA"
    encoded = rle_compress(sample_text)
    print(encoded)