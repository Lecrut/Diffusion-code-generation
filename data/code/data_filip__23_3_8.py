import itertools

def run_length_encode(text):
    if not text:
        return ""
    
    encoded_parts = []
    for char, group in itertools.groupby(text):
        count = len(list(group))
        encoded_parts.append(str(count) + char)
    
    return ''.join(encoded_parts)

if __name__ == '__main__':
    sample_text = "AAABBBCCD"
    result = run_length_encode(sample_text)
    print(result)
    
    sample_text2 = "ABC"
    result2 = run_length_encode(sample_text2)
    print(result2)
    
    sample_text3 = ""
    result3 = run_length_encode(sample_text3)
    print(result3)
    
    sample_text4 = "AAAAAAAAAABBBBBBBBBBBBCCCCCCCC"
    result4 = run_length_encode(sample_text4)
    print(result4)