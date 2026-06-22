import re

def run_length_encode(text):
    if not text:
        return ''
    
    encoded_chars = []
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded_chars.append(f"{text[i-1]}{count}")
            count = 1
            
    encoded_chars.append(f"{text[-1]}{count}")
    return ''.join(encoded_chars)

if __name__ == '__main__':
    sample_input = "aaabbc"
    result = run_length_encode(sample_input)
    print(result)