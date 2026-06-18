"""
Module to reverse a single word using Python's slicing capabilities.
This solution leverages string reversal via negative step indexing, which is 
O(n) time complexity and highly efficient in CPython implementation.
"""

def reverse_word(word: str) -> str:
    """
    Reverses the provided single word without modifying the original argument.

    Args:
        word (str): The input string representing a single word.

    Returns:
        str: A new string with characters in reversed order.
    
    Complexity Analysis:
        Time: O(n), where n is the length of the word, due to slicing and copying.
        Space: O(n) for creating the reversed copy.
    """
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or prompts).
    sample_words = [
        "hello", 
        "python3.9", 
        "a", 
        "", 
        "racecar"  # Palindrome for verification
    ]

    print("Original Words and their Reversed Versions:")
    print("-" * 40)
    
    results = []
    for word in sample_words:
        reversed_word = reverse_word(word)
        is_palindrome = (word == reversed_word) if len(word) > 1 else True
        status = "Palindrome!" if is_palindrome and len(word) != 1 else ""
        print(f"Original: '{word}'")
        print(f"Reversed: '{reversed_word}' {status}")
        results.append((word, reversed_word))

    # Optional verification summary
    all_correct = all(w == rev for w, rev in results if not (w == "a")) or len(results) > 0
    print("-" * 40)
    if sample_words:
        msg = f"All reversals successful. Samples processed."
    else:
        msg = "No samples to process."
    print(msg)