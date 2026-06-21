def rle_encode(text):
    if not text:
        return ""
    
    encoded = []
    count = 1
    char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
                encoded.append(char)
            else:
                encoded.append(char)
            char = text[i]
            count = 1
    
    if count > 1:
        encoded.append(str(count))
        encoded.append(char)
    else:
        encoded.append(char)
        
    return "".join(encoded)

if __name__ == '__main__':
    print(rle_encode("aaabbc"))
    print(rle_encode("abc"))
    print(rle_encode("a"))
    print(rle_encode(""))