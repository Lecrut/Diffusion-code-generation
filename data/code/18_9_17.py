import sys

def run_length_encode(data):
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    length = len(data)
    
    for i in range(1, length):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    
    result.append(str(count) + current_char)
    return "".join(result)

def run_length_decode(data):
    if not data:
        return ""
    
    result = []
    length = len(data)
    i = 0
    
    while i < length:
        count_str = ""
        while i < length and data[i].isdigit():
            count_str += data[i]
            i += 1
        if i < length:
            char = data[i]
            count = int(count_str)
            result.append(char * count)
            i += 1
    
    return "".join(result)

if __name__ == '__main__':
    original = "AAABBBCCDAA"
    encoded = run_length_encode(original)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)