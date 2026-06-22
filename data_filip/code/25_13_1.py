def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    return "".join(result)

def run_length_decode(encoded):
    if not encoded:
        return ""
    
    result = []
    i = 0
    while i < len(encoded):
        char = encoded[i]
        j = i + 1
        while j < len(encoded) and encoded[j].isdigit():
            j += 1
        count = int(encoded[i+1:j])
        result.append(char * count)
        i = j
    
    return "".join(result)

if __name__ == '__main__':
    sample = "AAABBBCCDAA"
    encoded = run_length_encode(sample)
    print(encoded)
    
    decoded = run_length_decode(encoded)
    print(decoded)
    
    empty_sample = ""
    print(run_length_encode(empty_sample))
    print(run_length_decode(""))
    
    single_char = "A"
    print(run_length_encode(single_char))
    print(run_length_decode(run_length_encode(single_char)))
    
    mixed_sample = "aabcccccaaa"
    print(run_length_encode(mixed_sample))
    print(run_length_decode(run_length_encode(mixed_sample)))