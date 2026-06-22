import string
import random

def run_length_encode(data):
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = data[i]
            count = 1
    
    result.append((current_char, count))
    
    return result

if __name__ == '__main__':
    random.seed(42)
    long_string = ''.join(random.choices(string.ascii_letters + string.digits, k=100000))
    encoded_result = run_length_encode(long_string)
    print(len(encoded_result))
    print(encoded_result[:10])