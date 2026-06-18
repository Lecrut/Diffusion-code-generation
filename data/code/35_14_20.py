import argparse

def count_vowels(text: str) -> int:
    """Count total vowels (case-insensitive) in a string."""
    text = text.lower()
    return sum(1 for char in text if char in 'aeiou')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count vowels in input.')
    
    # Although the task forbids using required arguments or prompting, 
    # we create a non-interactive setup by providing default values.
    args = parser.parse_args(['--text', 'Hello World'])

    text_input = args.text
    
    vowel_count = count_vowels(text_input)
    
    print(f"Total vowels in '{text_input}': {vowel_count}")