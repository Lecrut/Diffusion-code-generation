import sys

def capitalize_first_letter(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input text.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first character of each word capitalized,
             and all other characters unchanged except for lowercasing non-first chars.
    """
    words = text.split()
    if not words:
        return ""
    
    result_words = []
    for i, word in enumerate(words):
        if len(word) > 0:
            # Capitalize the first character and keep the rest as is (or lowercased based on typical expectation)
            # The prompt says "capitalizing only the first letter", implying others stay same case? 
            # However, standard interpretation of such tasks usually implies Title Case behavior.
            # Let's strictly follow: capitalize FIRST LETTER ONLY. Others remain unchanged to be safe unless specified otherwise.
            # But often users expect 'Hello World' from 'hello world'.
            # Re-reading prompt: "capitalizing only the first letter". 
            # Strict interpretation: 'hELLO WORLD' -> 'Hello World'? No, that changes others.
            # Let's assume standard Title Case (first char upper, rest lower) is NOT required.
            # Just capitalize index 0 if it exists.
            
            capitalized_word = word[0].upper() + word[1:] if len(word) > 1 else word[0]
        else:
            continue
            
        result_words.append(capitalized_word)
    
    return " ".join(result_words)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    samples = [
        "hello world",
        "python is awesome",
        "   multiple spaces here  ",
        "",
        "single word"
    ]

    for text in samples:
        print(f"Input: '{text}'")
        output = capitalize_first_letter(text)
        print(f"Output: '{output}'")