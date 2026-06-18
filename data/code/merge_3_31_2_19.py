def is_palindrome(text):
    """Check if a string (case-insensitive) reads the same forwards and backwards."""
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare cleaned text with its reverse
    return clean_text == clean_text[::-1]

def main():
    """Reads sample strings directly within this script without user interaction or command-line arguments."""
    
    test_cases = [
        "A man a plan a canal Panama",  # Should be True (case-insensitive, ignores spaces and punctuation)
        "No lemon no melon"             # Should be True
    ]

    print("Palindrome Check Results")
    print("-" * 40)
    
    for item in test_cases:
        result = is_palindrome(item)
        status_text = "IS a palindrome" if result else "Is NOT a palindrome"
        print(f"'{item}' {status_text}")

if __name__ == '__main__':
    main()