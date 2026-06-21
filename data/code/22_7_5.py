import re

def rle_decode(compressed: str) -> str:
    if not compressed:
        return ""
    
    result = []
    i = 0
    n = len(compressed)
    
    while i < n:
        char = compressed[i]
        if char.isdigit():
            j = i
            while j < n and compressed[j].isdigit():
                j += 1
            count = int(compressed[i:j])
            if i + 1 < n and not compressed[i + 1].isdigit():
                next_char = compressed[i + 1]
                result.append(next_char * count)
                i = j + 1
            else:
                i = j
        else:
            result.append(char)
            i += 1
            
    return "".join(result)

if __name__ == '__main__':
    compressed_input = "a12b3c4"
    decoded_output = rle_decode(compressed_input)
    print(decoded_output)