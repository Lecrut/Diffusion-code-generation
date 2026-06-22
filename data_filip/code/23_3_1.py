import itertools

def run_length_encode(text):
    if not text:
        return ""
    
    encoded_parts = []
    for char, group in itertools.groupby(text):
        count = sum(1 for _ in group)
        if count == 1:
            encoded_parts.append(char)
        else:
            encoded_parts.append(f"{count}{char}")
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_texts = [
        "AABBBCCDDDD",
        "ABC",
        "AAAAAAAA",
        "AABBCCDD",
        "",
        "X"
    ]
    
    for text in sample_texts:
        result = run_length_encode(text)
        print(result)