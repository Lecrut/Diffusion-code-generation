import argparse

def count_vowels(text: str) -> int:
    """Counts the total number of vowels in a given string (case-insensitive)."""
    return sum(1 for char in text if char.lower() in 'aeiouy')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count vowels in a word or sentence.')
    
    # Using optional arguments to avoid requiring user input via command line flags
    args, _ = parser.parse_known_args() 
    
    sample_inputs = [
        "hello world",
        "aeiouy is the vowel sound of English.",
        "Python 3.9 does not count 'y' as a universal vowel."
    ]
    
    for test_input in sample_inputs:
        vowel_count = count_vowels(test_input)
        print(f"Input: '{test_input}'")
        print(f"Total vowels (including y): {vowel_count}\n")