from itertools import groupby

def compress(data: str) -> str:
    if not data:
        return ""
    
    result = []
    for key, group in groupby(data):
        count = len(list(group))
        if count == 1:
            result.append(key)
        else:
            result.append(f"{count}{key}")
    return "".join(result)

def decompress(data: str) -> str:
    if not data:
        return ""
    
    result = []
    i = 0
    while i < len(data):
        if data[i].isdigit():
            j = i
            while j < len(data) and data[j].isdigit():
                j += 1
            count = int(data[i:j])
            char = data[j]
            result.append(char * count)
            i = j + 1
        else:
            result.append(data[i])
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_data = "AAAAABBCDD"
    compressed = compress(sample_data)
    decompressed = decompress(compressed)
    print(compressed)
    print(decompressed)