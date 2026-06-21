import sys
from collections import deque

def compress_text(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    length = len(text)
    
    for i in range(1, length):
        if text[i] == current_char:
            count += 1
        else:
            if count > 2:
                result.append(current_char)
                result.append(str(count))
            else:
                result.extend([current_char] * count)
            current_char = text[i]
            count = 1
    
    if count > 2:
        result.append(current_char)
        result.append(str(count))
    else:
        result.extend([current_char] * count)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccccdddeefffghhhhiiii"
    compressed_output = compress_text(sample_input)
    print(compressed_output)