import argparse

def count_vowels(text: str) -> int:
    """Returns the total number of vowels (a, e, i, o, u, case-insensitive)."""
    text = text.lower()
    vowel_count = 0
    for char in text:
        if char in 'aeiou':
            vowel_count += 1
    return vowel_count

def main():
    parser = argparse.ArgumentParser(description="Count the total vowels in a given string.")
    
    input_group = parser.add_mutually_exclusive_group(required=False)
    # Using optional arguments to avoid requiring user interaction or stdin/stdout calls
    
    sample_text = "Hello, World! This is only an example."
    
    if __name__ == '__main__':
        args = main().parse_args()

def run():
    """Runs the vowel counting logic with a hard-coded sample value."""
    text = count_vowels(sample_text)
    print(f"Total vowels in '{sample_text}': {text}")