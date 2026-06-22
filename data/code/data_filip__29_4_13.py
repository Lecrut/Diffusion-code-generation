def run_length_encode(text):
    if not text:
        return ""
    
    result = []
    char_buffer = []
    count = 0
    previous_char = None
    
    for char in text:
        if char == previous_char:
            count += 1
        else:
            if count > 3:
                result.append(str(count))
                result.append(previous_char)
            elif count > 0:
                result.append(str(count))
                for _ in range(count):
                    result.append(previous_char)
            
            previous_char = char
            count = 1
            
    if count > 3:
        result.append(str(count))
        result.append(previous_char)
    elif count > 0:
        result.append(str(count))
        for _ in range(count):
            result.append(previous_char)
            
    return "".join(result)

def run_length_decode(encoded_text):
    if not encoded_text:
        return ""
    
    result = []
    i = 0
    length = len(encoded_text)
    
    while i < length:
        if encoded_text[i].isdigit():
            j = i
            while j < length and encoded_text[j].isdigit():
                j += 1
            count = int(encoded_text[i:j])
            if j < length:
                char = encoded_text[j]
                result.append(char * count)
                i = j + 1
            else:
                result.append(encoded_text[j-1] * count)
                i = j
        else:
            result.append(encoded_text[i])
            i += 1
            
    return "".join(result)

if __name__ == '__main__':
    original = "AAABBBCCCCDDDEEEFFFFGGGGGGHHHHH"
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)
    print(original == decoded)