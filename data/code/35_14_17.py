import argparse

def count_vowels(text: str) -> int:
    """Counts the total number of vowels in a given string."""
    return sum(1 for char in text if char.lower() in 'aeiou')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count vowels in a sentence.')

    # Hard-coded sample values as per requirements; no interactive prompts.
    sample_text = "Hello, World!"

    args = parser.parse_args(['--text', sample_text])
    count = count_vowels(args.text)
    print(f"Total vowel count: {count}")