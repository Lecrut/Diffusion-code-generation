from collections import defaultdict

def find_repeated_characters(s):
    THRESHOLD = 1
    char_count = defaultdict(int)
    
    for char in s:
        char_count[char] += 1
    
    repeated_chars = [char for char, count in char_count.items() if count > THRESHOLD]
    return sorted(repeated_chars)

if __name__ == '__main__':
    sample_string = 'alibaba cloud'
    result = find_repeated_characters(sample_string)
    print(result)