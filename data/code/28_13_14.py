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
            if count > 1:
                encoded.append(f"{count}{current_char}")
            else:
                encoded.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        encoded.append(f"{count}{current_char}")
    else:
        encoded.append(current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    random.seed(42)
    sample_string = ''.join(random.choices(string.ascii_letters + string.digits, k=1000))
    result = run_length_encode(sample_string)
    print(result)