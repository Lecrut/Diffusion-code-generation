import string
import random

def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def run_length_decode(encoded):
    decoded = []
    i = 0
    while i < len(encoded):
        if not encoded[i].isdigit():
            return decoded[0] if decoded else ""
        
        num_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1
        
        if i >= len(encoded):
            return decoded[0] if decoded else ""
        
        count = int(num_str)
        char = encoded[i]
        decoded.append(char * count)
        i += 1
    
    return "".join(decoded)

if __name__ == '__main__':
    random.seed(42)
    alphabet = string.ascii_letters + string.digits + string.punctuation
    test_string = ''.join(random.choices(alphabet, k=10000))
    
    encoded_result = run_length_encode(test_string)
    print(f"Encoded length: {len(encoded_result)}")
    print(f"Original length: {len(test_string)}")
    
    decoded_result = run_length_decode(encoded_result)
    print(f"Decode successful: {decoded_result == test_string}")