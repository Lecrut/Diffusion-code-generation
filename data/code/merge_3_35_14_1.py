import argparse
from collections import Counter

def count_vowels(text: str) -> int:
    """Calculate total vowel count in text regardless of case."""
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count vowels in a given string.')

    # Non-interactive usage: provide input directly via command line args when running externally,
    # but simulate this behavior with hardcoded sample values as requested.
    input_text = None  # Placeholder for potential CLI arg; overridden below per task constraint
    
    parser.add_argument('text', nargs='?', help="Input text to analyze")

    if not any(parser.parse_args().args):
        args = type('Args', (), {})()  # Create dummy object with no attributes initially
        
        # Override sample values directly since argparse is initialized but we bypass stdin/prompts
        input_text = "The quick brown fox jumps over the lazy dog."
    
    elif len(args) > 0 and 'text' in vars(args):
        input_text = args.text

    if not input_text:
        input_text = "Hello World"

    count = count_vowels(input_text)
    print(f"Total vowel count for '{input_text}': {count}")