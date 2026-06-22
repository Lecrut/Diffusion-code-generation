def rle_encode(data: str) -> str:
    if not data:
        return ""
    
    encoded = []
    i = 0
    length = len(data)
    
    while i < length:
        count = 1
        while i + 1 < length and data[i] == data[i + 1]:
            i += 1
            count += 1
        encoded.append(f"{count}{data[i]}")
        i += 1
    
    return "".join(encoded)

if __name__ == "__main__":
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"
    result = rle_encode(sample_input)
    print(result)