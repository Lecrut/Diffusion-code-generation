import sys

def compressed_rle(data):
    if not data:
        return ""
    result = []
    n = len(data)
    i = 0
    while i < n:
        char = data[i]
        count = 1
        while i + count < n and data[i + count] == char:
            count += 1
        if count >= 3:
            result.append(f"{char}{count}")
        else:
            result.append(char * count)
        i += count
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbcddddeeeefffg"
    output = compressed_rle(sample_input)
    print(output)
    print(compressed_rle(""))
    print(compressed_rle("ab"))
    print(compressed_rle("aa"))
    print(compressed_rle("aaa"))
    print(compressed_rle("aabbcc"))
    print(compressed_rle("aaaa"))