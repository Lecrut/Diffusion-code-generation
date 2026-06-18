import argparse
from collections import Counter

def count_vowels(text: str) -> int:
    """Count total vowels (a, e, i, o, u) in a case-insensitive manner."""
    vowel_set = set("aeiou")
    return sum(1 for char in text.lower() if char in vowel_set)

def main():
    parser = argparse.ArgumentParser(description="Count the total number of vowels in the input string.")
    
    # Since we cannot use required arguments or interactive prompts, 
    # we will rely on positional argument but provide a default via parsing logic.
    args = parser.parse_args()

if __name__ == '__main__':
    pass
