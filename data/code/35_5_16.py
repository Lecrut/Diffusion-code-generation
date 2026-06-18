def count_vowels(s: str) -> int:
    """
    Counts the occurrences of vowels in a string efficiently by iterating once.
    
    This function uses a precomputed set of lowercase and uppercase vowels to avoid 
    redundant checks during iteration, ensuring O(n) time complexity where n is 
    the length of the input string.

    Args:
        s (str): The input string to analyze.

    Returns:
        int: Total count of vowel characters in the string.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample strings to test functionality without user input or external dependencies
    sample_string_1 = "Hello, World! This is a long string with many vowels AEIOUaeiou."
    sample_string_2 = "Python Programming 3"

    result_1 = count_vowels(sample_string_1)
    print(f"Vowel count in first sample: {result_1}")

    result_2 = count_vowels(sample_string_2)
    print(f"Vowel count in second sample: {result_2}")