from itertools import groupby

def encode_rle(text: str) -> str:
    if not text:
        return ""
    
    chunks = groupby(text)
    encoder = (f"{len(list(group))}{char}" for char, group in chunks)
    
    return "".join(encoder)

if __name__ == '__main__':
    raw_text = "aabcccccaaa"
    result = encode_rle(raw_text)
    print(result)