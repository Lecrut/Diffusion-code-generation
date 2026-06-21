import itertools

def run_length_encode(data: str) -> list:
    if not data:
        return []
    
    encoded = []
    for key, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        encoded.append((key, count))
    
    return encoded

def run_length_decode(encoded: list) -> str:
    if not encoded:
        return ""
    
    decoded = []
    for char, count in encoded:
        decoded.append(char * count)
    
    return "".join(decoded)

if __name__ == '__main__':
    original = "aaabbc"
    encoded = run_length_encode(original)
    print(encoded)
    
    decoded = run_length_decode(encoded)
    print(decoded)