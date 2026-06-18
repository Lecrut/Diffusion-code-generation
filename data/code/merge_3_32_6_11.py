# Length Calculator Module #!/usr/bin/env python3
"""A simple module to calculate phrase length using hardcoded values."""

def get_phrase_length(phrase: str) -> int:
    """Calculate and return the exact character length of a given phrase.
    
    Args:
        phrase (str): The input string for which length is required.

    Returns:
        int: The number of characters in the provided phrase.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hardcoded sample values to ensure no user interaction or file access is needed.
    samples = [
        "Hello, World!",  # Expected length: 13 (including comma and exclamation mark)
        "Python Programming",  # Expected length: 19
        "",                 # Edge case: Empty string, expected length: 0
    ]

    for phrase in samples:
        result = get_phrase_length(phrase)
        print(f"Length of '{phrase}': {result}")