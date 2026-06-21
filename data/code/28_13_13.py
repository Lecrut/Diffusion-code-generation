import random
import string

def run_length_encode(data):
    if not data:
        return ""
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = data[i]
            count = 1
    
    encoded.append((current_char, count))
    
    result_parts = []
    for char, count in encoded:
        result_parts.append(f"{count}{char}")
    
    return "".join(result_parts)

if __name__ == '__main__':
    random.seed(42)
    long_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10000))
    encoded_result = run_length_encode(long_string)
    print(encoded_result)