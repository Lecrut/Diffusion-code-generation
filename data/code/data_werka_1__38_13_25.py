def process_string(s):
    letter_count = {}
    for char in s:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_count:
                letter_count[char_lower] += 1
            else:
                letter_count[char_lower] = 1
    
    THRESHOLD = 1
    repeated_letters = {char: count for char, count in letter_count.items() if count > THRESHOLD}
    return repeated_letters

if __name__ == '__main__':
    sample_string1 = "hello world"
    sample_string2 = "programming is fun"
    sample_string3 = "Alibaba Cloud"
    result1 = process_string(sample_string1)
    result2 = process_string(sample_string2)
    result3 = process_string(sample_string3)
    print(result1)
    print(result2)
    print(result3)