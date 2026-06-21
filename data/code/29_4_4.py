import re
from functools import reduce

def compress_text(text):
    if not text:
        return ""
    
    chunks = []
    i = 0
    n = len(text)
    
    while i < n:
        char = text[i]
        count = 1
        
        while i + count < n and text[i + count] == char:
            count += 1
        
        if count >= 4:
            chunks.append(f"{count}{char}")
            i += count
        else:
            while i < n and (count < 4 or text[i] != text[i + 1] if i + 1 < n else True):
                current_count = 1
                while i + current_count < n and text[i + current_count] == text[i] and current_count < 4:
                    current_count += 1
                if current_count >= 4:
                    break
                for _ in range(current_count):
                    chunks.append(text[i])
                i += current_count
                break
            else:
                if i < n:
                    chunks.append(text[i])
                    i += 1
    
    return "".join(chunks)

if __name__ == '__main__':
    sample = "aaabbbccccddddeeefffff"
    result = compress_text(sample)
    print(result)