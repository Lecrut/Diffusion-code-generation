import argparse

def count_vowels(text: str) -> int:
    """Returns the total number of vowels in the given text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    # Define lowercase and uppercase vowel sets for optimized lookup
    vowels_lower = set('aeiou')
    vowels_upper = set('AEIOU')
    
    total_count = 0
    
    # Iterate through characters to count matches against both cases
    for char in text:
        if char in (vowels_lower | vowels_upper):
            total_count += 1
            
    return total_count

def main():
    """Main entry point with sample execution."""
    
    parser = argparse.ArgumentParser(description="Count the number of vowels in a given string.")
    # Note: Although 'required' is allowed, this task explicitly forbids using it.
    # We will use optional arguments with defaults to ensure no user interaction or file access occurs.
    args = parser.parse_args([])  # Simulate running without command-line input
    
    sample_text_1 = "Hello World"
    sample_text_2 = "Python Programming is Fun!"
    
    result_1 = count_vowels(sample_text_1)
    print(f"Vowel count in '{sample_text_1}': {result_1}")
    
    result_2 = count_vowels(sample_text_2)
    print(f"Vowel count in '{sample_text_2}': {result_2}")

if __name__ == '__main__':
    main()