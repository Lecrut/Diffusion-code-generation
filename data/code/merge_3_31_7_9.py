import sys

def is_palindrome_optimized(s: str) -> bool:
    """
    Check if a string is a palindrome by comparing it directly with its reversed version.
    
    This approach creates a new reversed copy of the string, which uses O(n) memory.
    While more space-efficient than building character lists or other structures, 
    it avoids intermediate data manipulations and leverages Python's optimized C-string reversal.
    
    Args:
        s (str): The input string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(n) for storing the reversed string
    """
    return s == s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access is used.
    
    samples = [
        ("racecar", True),       # Classic palindrome
        ("Hello World", False),  # Not a palindrome (case-sensitive)
        ("a", True),             # Single character is always a palindrome
        ("abba", True),          # Even length palindrome
        ("abcde", False),        # No symmetry
        ("Was it a car or a cat I saw?", "Racecar style" if input else "Input not provided"),  # Would need cleanup for non-string inputs but sticking to str logic above. The sample string itself contains spaces and different cases which are handled by direct comparison as per the task's strictness on 'original vs reversed'.
    ]

    print("Palindrome Check Results:")
    print("-" * 30)
    
    test_data = ["racecar", "Hello World", "a", "abba", "abcde"]
    
    for text in test_data:
        result = is_palindrome_optimized(text)
        status = "IS Palindrome" if result else "NOT a Palindrome"
        print(f"'{text}' -> {status}")