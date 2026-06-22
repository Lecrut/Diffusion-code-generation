def rle_encode(data):
    if not data:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded.append(str(count) + data[i - 1])
            count = 1
    encoded.append(str(count) + data[-1])
    return "".join(encoded)

def rle_decode(data):
    if not data:
        return ""
    decoded = []
    i = 0
    while i < len(data):
        count = ""
        while i < len(data) and data[i].isdigit():
            count += data[i]
            i += 1
        if i < len(data):
            char = data[i]
            decoded.append(char * int(count))
            i += 1
    return "".join(decoded)

def bidirectional_rle_process(input_string):
    compressed = rle_encode(input_string)
    decompressed = rle_decode(compressed)
    return compressed, decompressed

if __name__ == "__main__":
    sample = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result_compressed, result_decompressed = bidirectional_rle_process(sample)
    print(f"Original: {sample}")
    print(f"Compressed: {result_compressed}")
    print(f"Decompressed: {result_decompressed}")