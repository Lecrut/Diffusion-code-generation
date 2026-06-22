def rle_compress(text):
    if not text:
        return ""
    
    result = []
    count = 1
    length = len(text)
    
    for i in range(1, length):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(f"{count}{text[i - 1]}")
            count = 1
    
    result.append(f"{count}{text[-1]}")
    return "".join(result)

if __name__ == '__main__':
    input_string = "AAABBBCCCDAA"
    compressed_output = rle_compress(input_string)
    print(compressed_output)