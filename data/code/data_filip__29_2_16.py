def run_length_encode(s):
    if not s:
        return ""
    
    encoded_parts = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded_parts.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    
    encoded_parts.append(str(count) + current_char)
    return "".join(encoded_parts)

if __name__ == '__main__':
    samples = [
        "aaabbc",
        "aabcccccaaa",
        "abcdef",
        "",
        "a",
        "pppppppppppppppwwwwwwwwwweeeerrrrrrrrr"
    ]
    
    for sample in samples:
        result = run_length_encode(sample)
        print(result)