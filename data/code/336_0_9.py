def check_repeated_chars(text: str) -> bool:
    cleaned_text = text.lower()
    seen_characters = set()
    for char in cleaned_text:
        if char not in ' \t\n':                     
            if char in seen_characters:
                return True
            seen_characters.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "Hello World",                                                 
        "Python Programming",                                                                                                                        
        "aaaaa",                                
        "The Quick Brown Fox Jumps Over The Lazy Dog"                          
    ]
    for test_string in sample_strings:
        result = check_repeated_chars(test_string)
        print(f"'{test_string}': {'Contains repeated characters' if result else 'No repeated characters'}")