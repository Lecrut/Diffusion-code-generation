import collections

def compress_binary_string(raw: str) -> str:
    if raw is None:
        return ""
    if not raw:
        return ""
    
    segments = []
    counter = collections.Counter(raw)
    last_char = None
    current_run = 0
    
    for char in raw:
        if char == last_char:
            current_run += 1
        else:
            if last_char is not None:
                segments.append((last_char, current_run))
            last_char = char
            current_run = 1
    if last_char is not None:
        segments.append((last_char, current_run))
        
    if not segments:
        return ""
    
    parts = []
    for char, count in segments:
        parts.append(f"{char}{count}")
    return "".join(parts)

if __name__ == '__main__':
    test_cases = [
        "1100011110",
        "1",
        "",
        "0000",
        "010101"
    ]
    
    for case in test_cases:
        result = compress_binary_string(case)
        print(f"Input: '{case}' -> Output: '{result}'")