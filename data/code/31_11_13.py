def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome ignoring spaces, punctuation, and case."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    test_cases = [
        "A man a plan a canal Panama",
        "race car",
        "Hello, World!",
        "Madam",
        "Python 3"
    ]

    print("Palindrome Checker - Sample Tests")
    print("-" * 40)

    for test_string in test_cases:
        result = is_palindrome(test_string)
        status = "Is a palindrome!" if result else ""
        # Using f-string within the function call logic, but keeping it simple here.
        output_message = f'"{test_string}" {status}'
        
        print(output_message)

    # Demonstration with user interaction logic commented out as per constraints 
    # (No actual input() calls are made).