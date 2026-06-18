def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Create a cleaned version of the string containing only alphanumeric characters in lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    # Use two-pointer approach for O(n) time and O(1) additional space (excluding input storage)
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
        
    return True

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a cat and I saw a bad?cat", "Yes" if is_palindrome("was it a cat and i saw a cat") else "No"), # Testing logic manually here since the string has extra words, let's fix for clarity below
    ]

    correct_samples = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a card! I saw a sad cat?", True), # "wasitacardi" reversed is same ignoring case/punctuation -> wasitaicardiwassadcat... wait. 
             # Correct palindrome test string: "A man, a plan: Capital Panama!"
    ]

    final_tests = [
        ("racecar", True),
        ("No 'x' in Nixon!", False),
        ("Was it a car I saw? Yes I did.", True) # wasitacaridesawyesidid -> reversed same ignoring case/punct. 
           # Let's trace: "wasitacardiwased" ? No.
           # Correct: "A man, a plan, a canal: Panama" is standard.
    ]

    test_cases = [
        ("racecar", True),
        ("No 'x' in Nixon!", False),
        ("Was it a car I saw?", False), 
        ("Madam", True),
        ("Trusted man was no matter, just not.", False) # t r u s t e d m a n w a s ... reversed != original
    
    ]

    additional_tests = [
         "A man a plan canal Panama!",
     ]

    test_cases.append(("A man a plan canal Panama!", True))
    
    for text, expected in test_cases: 
        result = is_palindrome(text)
        print(f"Input: '{text}' -> Expected: {expected}, Got: {result}")

    # Run one more specific complex case manually to ensure correctness without printing logic errors on bad manual traces
    
    if __name__ == '__main__':
         text_to_check = "A man, a plan, a canal: Panama" 
         print(f"\nFinal Check - '{text_to_check}': {is_palindrome(text_to_check)}")