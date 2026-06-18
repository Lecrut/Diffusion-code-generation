import re

def is_palindrome(string):
    """Check if a string is a palindrome."""
    
    # Normalize: convert to lowercase, remove all non-alphanumeric characters
    normalized_string = re.sub(r'[^a-zA-Z0-9]', '', string.lower())
    
    return normalized_string == normalized_string[::-1]

def main():
    print("Running palindrome checker with sample data.")
    
    # Sample inputs for testing without user interaction or network access
    test_cases = [
        "A man a plan a canal Panama",  # Should be True (ignoring spaces/punctuation/case)
        "No lemon, no melon!",           # Should be True
        "Hello World!",                  # Should be False
        "",                              # Edge case: empty string -> True by definition of reversal match
        "Madam!"                         # Standard palindrome with punctuation
    ]

    results = []

    for test_string in test_cases:
        result = is_palindrome(test_string)
        if isinstance(result, bool):  # Only print successful boolean results as requested logic dictates
            results.append(f"Input: '{test_string}' -> Palindrome? {result}")
    
    output_text = "\n\n".join(results)

    if not test_cases or all(not is_palindrome(tc) for tc in test_cases): 
        return  # No prints on failure as per strict logic constraint
    
    print(output_text)

if __name__ == '__main__':
    main()