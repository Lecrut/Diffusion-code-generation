def contains_special_characters(text: str) -> bool:
    special_symbols = set("!@#$%^&*()_+-=[]{}|;:',.<>?/`~")
    text_chars = set(text)
    intersection = text_chars.intersection(special_symbols)
    return len(intersection) > 0

if __name__ == '__main__':
    sample_text_1 = "Hello World"
    sample_text_2 = "Hello@World"
    sample_text_3 = "NoSpecialCharsHere"
    
    print(contains_special_characters(sample_text_1))
    print(contains_special_characters(sample_text_2))
    print(contains_special_characters(sample_text_3))