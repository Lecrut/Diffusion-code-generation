import random
import string

def run_length_encode(s):
    if not s:
        return ''
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    
    encoded.append((current_char, count))
    
    return ''.join(f"{char}{count}" for char, count in encoded)

def generate_random_string(length=1000):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == '__main__':
    random_string = generate_random_string(10000)
    encoded_result = run_length_encode(random_string)
    print(len(encoded_result))