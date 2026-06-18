import string

def count_vowels(text: str) -> int:
    """
    Count the total number of vowels (a, e, i, o, u - case insensitive).
    Uses a set lookup for optimized O(1) average time complexity.
    
    :param text: The input string to analyze.
    :return: An integer representing the count of vowels.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

def run_sample():
    """Executes a single test case with hardcoded sample values as per requirements."""
    sample_input = "Hello, World! This is a simple test sentence."
    result = count_vowels(sample_input)
    print(f"Total vowel count: {result}")

if __name__ == '__main__':
    run_sample()