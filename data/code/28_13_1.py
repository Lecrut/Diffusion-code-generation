import sys

def run_length_encode(data: str) -> list:
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

def run_length_decode(encoded_data: list) -> str:
    result = []
    for char, count in encoded_data:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    import random
    import string
    random.seed(42)
    source_chars = string.ascii_letters + string.digits
    sample_string = ''.join(random.choice(source_chars) for _ in range(500))
    
    encoded = run_length_encode(sample_string)
    decoded = run_length_decode(encoded)
    
    print(f"Original length: {len(sample_string)}")
    print(f"Encoded tuples: {len(encoded)}")
    print(f"Decoded matches original: {decoded == sample_string}")
    print(f"First 5 encoded tuples: {encoded[:5]}")
    print(f"Decoded string (first 50 chars): {decoded[:50]}")