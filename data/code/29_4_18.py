import sys
import io

def compress_text(text):
    if not text:
        return ""
    
    output = io.StringIO()
    n = len(text)
    i = 0
    
    while i < n:
        count = 1
        while i + 1 < n and text[i] == text[i + 1]:
            count += 1
            i += 1
        
        output.write(text[i])
        output.write(str(count))
        i += 1
    
    return output.getvalue()

if __name__ == '__main__':
    sample_text = "aaabbbccccdddeee"
    result = compress_text(sample_text)
    print(result)