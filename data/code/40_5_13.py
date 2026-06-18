def get_first_letters(word_string):
    import re
    
    # Find all sequences of alphabetic characters in the string
    words = re.findall(r'[a-zA-Z]+', word_string)
    
    result_dict = {}
    for word in words:
        if not word:  # Safety check, though regex ensures non-empty
            continue
        
        first_char = word[0].lower()
        
        # The prompt says "keys are the words". Should we lowercase keys? 
        # Usually yes to be consistent with values being lowercased letters.
        result_dict[word.lower()] = first_char
        
    return result_dict

if __name__ == '__main__':
    sample_input_1 = "Hello, world! How are you?"
    sample_input_2 = "'twas the night before christmas"
    
    # Test cases hard-coded as per requirement (no user input)
    test_cases = [
        ("Hello, world!", {"hello": "h", "world": "w"}),
        ("O'Connor is great.", {"oconnor": "o", "is": "i", "great": "g"}) # Assuming O and Connor are one block due to apostrophe? 
    ]

    # Let's refine the regex logic for 'O\'Connor'. 
    # [a-zA-Z]+ will match 'O', then skip ', then 'Connor' -> keys: o, connor.
    # This seems reasonable as punctuation breaks words in simple tokenization unless specified otherwise.
    
    print("Sample 1:", get_first_letters(sample_input_1))
    print("Sample 2:", get_first_letters("'twas the night before christmas"))