import re

def rle_decode(compressed: str) -> str:
    if not compressed:
        return ''
    
    result = []
    i = 0
    n = len(compressed)
    
    while i < n:
        char = compressed[i]
        i += 1
        if i < n and compressed[i].isdigit():
            j = i
            while j < n and compressed[j].isdigit():
                j += 1
            count_str = compressed[i:j]
            count = int(count_str)
            i = j
            result.append(char * count)
        else:
            result.append(char)
    
    return ''.join(result)

if __name__ == '__main__':
    sample_input = 'A3B2C'
    decoded_output = rle_decode(sample_input)
    print(decoded_output)