def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    parts = []
    start = 0
    
    while start < len(text):
        current_char = text[start]
        end = start + 1
        
        while end < len(text) and text[end] == current_char:
            end += 1
            
        count = end - start
        parts.append(str(count) + current_char)
        start = end
        
    return "".join(parts)

if __name__ == '__main__':
    sample = "AAAABBBCCDAA"
    output = run_length_encode(sample)
    print(output)