def rle_compress(data: str) -> str:
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    result = rle_compress(sample_input)
    print(result)