def run_length_encode(text):
    if not text:
        return ""
    
    def encoder_gen(s):
        if not s:
            return
        current = s[0]
        count = 1
        for char in s[1:]:
            if char == current:
                count += 1
            else:
                yield (current, count)
                current = char
                count = 1
        yield (current, count)
    
    parts = []
    for char, count in encoder_gen(text):
        parts.append(f"{char}{count}")
    return "".join(parts)

def run_length_decode(encoded):
    if not encoded:
        return ""
    
    def decoder_gen(s):
        i = 0
        n = len(s)
        while i < n:
            if not s[i].isalpha() and not s[i].isascii():
                raise ValueError("Invalid character")
            char = s[i]
            i += 1
            num_str = ""
            while i < n and s[i].isdigit():
                num_str += s[i]
                i += 1
            if not num_str:
                raise ValueError("Missing count")
            count = int(num_str)
            yield (char, count)
    
    parts = []
    try:
        for char, count in decoder_gen(encoded):
            parts.append(char * count)
    except ValueError:
        return None
    return "".join(parts)

if __name__ == '__main__':
    sample_input = "AAABBBCCCDAA"
    encoded = run_length_encode(sample_input)
    decoded = run_length_decode(encoded)
    print(f"Original: {sample_input}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Match: {sample_input == decoded}")