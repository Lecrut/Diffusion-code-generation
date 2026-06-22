CHAR_MAP = {chr(i): chr(i) for i in range(32, 127)}

def run_length_encode(source):
    if not source:
        return ""
    
    segments = []
    current_char = source[0]
    current_count = 1
    
    for idx in range(1, len(source)):
        char_at_pos = source[idx]
        if char_at_pos == current_char:
            current_count += 1
        else:
            mapped_char = CHAR_MAP.get(current_char, current_char)
            segments.append(f"{mapped_char}{current_count}")
            current_char = char_at_pos
            current_count = 1
            
    mapped_char = CHAR_MAP.get(current_char, current_char)
    segments.append(f"{mapped_char}{current_count}")
    
    return "".join(segments)

if __name__ == '__main__':
    test_input = 'hello'
    result = run_length_encode(test_input)
    print(result)