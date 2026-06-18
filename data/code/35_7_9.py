import string

def count_vowels(word: str) -> int:
    """Count total vowels in a given word."""
    if not isinstance(word, str):
        raise TypeError("Input must be a string.")
    
    word = word.lower()
    return sum(1 for char in word if char in "aeiou")

if __name__ == '__main__':
    sample_word = "Hello World"
    vowel_count = count_vowels(sample_word)
    print(f"The total vowel count in '{sample_word}' is {vowel_count}.")