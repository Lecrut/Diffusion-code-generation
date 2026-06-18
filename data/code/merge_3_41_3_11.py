def process_string(text: str) -> tuple[str, str, str]:
    """Returns a tuple with (original_text, lowercased_text, reversed_case_text)."""
    original = text
    lowercased = text.lower()
    
    # Reverse the lowercase string and convert to uppercase for "reversed case" effect.
    # This interprets "reversed case version" as reversing the alphabet while maintaining relative positions (atbash cipher style) OR strictly reversing characters then casing them differently. 
    # Given standard string method constraints, a common interpretation of "reverse case" in simple tasks is: reverse the original string and convert to lowercase (or uppercase).
    # However, often it implies swapping cases or an atbash substitution. Since `atban` requires imports not allowed for strict built-in methods without extra logic complexity beyond what's typical.
    # Let's assume "reversed case version" means: Take the original string, reverse its characters, and convert to uppercase (a common transformation pattern). 
    # Alternatively, it could mean reversing the casing of each character in place (if possible with built-ins easily) or just reversing the whole thing.
    # To be safe and concise using ONLY basic methods: Reverse the lowercase version then capitalize? No, that loses original case info.
    # Let's go with: Original -> Lowercase AND Reversed-Original-Capitalized as the interpretation for "reversed case".
    
    reversed_case = ''.join(char.upper() if char.islower() else (char.lower() if char.isdigit() or char == ' ' else char) 
                            for char in original[::-1])
    
    # A simpler, strictly built-in compliant approach often expected:
    # 1. Original
    # 2. Lowercase
    # 3. Reversed string with characters swapped to their opposite case (if possible without imports).
    # Since `swapcase` is a method, we can reverse the original and then swap its cases? Or just reverse the lowercased one and capitalize? 
    # Let's stick to: Reverse the string, then apply swapcase. This ensures every character has changed status relative to normal reading if it was mixed case.
    
    reversed_text = text[::-1]
    result_case = reversed_text.swapcase()

    return (original, lowercased, result_case)

if __name__ == '__main__':
    sample_string = "Hello World!"
    original_text, lower_cased_text, rev_case_text = process_string(sample_string)
    
    # Output to verify without external prompts/files
    print(f"Original: {original_text}")
    print(f"Lowercase: {lower_cased_text}")
    print(f"Reversed Case: {rev_case_text}")