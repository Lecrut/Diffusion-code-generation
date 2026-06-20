SPECIAL_CHARACTERS = set('!@#$%^&*()_+-=[]{}|;:,.<>?/~`')

def contains_special_characters(text):
    if not text:
        return False
    text_chars = set(text)
    intersection = text_chars.intersection(SPECIAL_CHARACTERS)
    return len(intersection) > 0

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "hello@world"
    sample3 = "12345!"
    sample4 = ""
    
    result1 = contains_special_characters(sample1)
    result2 = contains_special_characters(sample2)
    result3 = contains_special_characters(sample3)
    result4 = contains_special_characters(sample4)
    
    print(result1)
    print(result2)
    print(result3)
    print(result4)