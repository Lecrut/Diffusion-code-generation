import unicodedata

def is_consonant(char):
    if not char.isalpha():
        return False
    if char.lower() in 'aeiou':
        return False
    return True

def count_consonants(text):
    count = 0
    normalized_text = unicodedata.normalize('NFC', text)
    for char in normalized_text:
        if is_consonant(char):
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello, World! 你好世界 café ñ"
    result = count_consonants(sample_string)
    print(result)