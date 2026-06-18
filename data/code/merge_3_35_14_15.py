import argparse

def count_vowels(text: str) -> int:
    """Counts total vowels (a, e, i, o, u, A, E, I, O, U) in the input string."""
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

def main():
    parser = argparse.ArgumentParser(description='Count total vowels in a given word or sentence.')
    
    # Although 'input()' and interactive prompts are forbidden, 
    # the task requires using `argparse`. We provide a sample input via command-line args
    # to satisfy the requirement of running without user interaction.
    parser.add_argument('text', type=str, help='The word or sentence to analyze.')
    
    if len(sys.argv) == 1:
        sys.exit(0)

if __name__ == '__main__':
    import sys
    
    # Hard-coded sample values as per instructions (simulating command-line args for non-interactive run)
    parser = argparse.ArgumentParser(description='Count total vowels in a given word or sentence.')
    
    example_words = [
        "Hello", 
        "AEIOU", 
        "Python is great!", 
        "aeiou"
    ]
    
    # We iterate through examples to demonstrate functionality without user input.
    for sample_text in example_words:
        args, remaining = parser.parse_args([sample_text])
        vowel_count = count_vowels(args.text)
        print(f"Input: '{args.text}'")
        print(f"Total vowels: {vowel_count}")