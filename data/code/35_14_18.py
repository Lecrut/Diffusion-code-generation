import argparse

def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The total count of vowels found in the string.
    """
    # Define lowercase and uppercase vowels for optimized lookup
    vowel_set = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowel_set)

def main():
    parser = argparse.ArgumentParser(description="Count total vowels in a provided word or sentence.")
    
    # Although the task forbids 'required' arguments, we use an optional argument 
    # to comply with standard CLI practices while avoiding mandatory prompts.
    input_text = None
    
    if len(sys.argv) > 1:
        input_text = sys.argv[1]

    if not input_text and count_vowels(""):
        print(f"Vowel count for sample '': {count_vowels('')}")
        
    elif not input_text:
        # Fallback to hard-coded samples as per the requirement 
        # since no arguments were passed.
        samples = ["Hello", "Python Programming"]
        total_count = 0
        
        print("Running with sample values (no user input):")
        for word in samples:
            count = count_vowels(word)
            print(f"Word '{word}': {count} vowel(s)")
            total_count += count
            
        print(f"\nTotal vowels across all samples: {total_count}")

if __name__ == '__main__':
    import sys
    
    # Ensure we don't block if run without arguments, but the logic above handles it.
    main()