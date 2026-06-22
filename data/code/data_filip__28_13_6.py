import random
import string

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
            encoded.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    
    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == '__main__':
    random.seed(42)
    hardcoded_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10000))
    result = run_length_encode(hardcoded_string)
    print(result)