import string

def find_repeated_letters(text: str) -> dict[str, int]:
    """
    Counts occurrences of each letter (case-insensitive, ignoring non-alphabetic characters).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        dict[str, int]: A dictionary mapping unique repeated letters to their counts.
                       Only includes letters with a count > 1. Keys are lowercase strings.
    """
    letter_counts = {}
    
    # Normalize text to lower case for comparison but preserve non-alphabetic logic implicitly by skipping them
    normalized_text = text.lower()
    
    for char in normalized_text:
        if 'a' <= char <= 'z':  # Check if character is an alphabetic letter
            current_count = letter_counts.get(char, 0) + 1
            letter_counts[char] = current_count
            
    return {letter: count for letter, count in letter_counts.items() if count > 1}

def main():
    """Main execution block that processes sample inputs without external prompts."""
    
    # Sample input strings to test the function robustly
    samples = [
        "Hello World!",           # Contains 'l' (3), 'o' (2) - note: spaces/punctuation ignored
        "A man, a plan, a canal: Panama",  # Palindrome structure, many repeats like 'a', 'n', etc.
        "Python is awesome.",    # Repeats: 'e', 's'
        "",                       # Empty string edge case
        "123 !@#"                 # No letters expected
    ]
    
    output_results = []
    
    for sample_input in samples:
        repeated_letters = find_repeated_letters(sample_input)
        
        if not is_substring_in_sample(r := str(repeated_letters)):
            print(f"\nInput String:\n{sample_input!r}\n")
            
            # Check the result dictionary directly instead of relying on implicit substring checks within strings, 
            # since a string might contain 'a' by accident. We verify if there are any keys in our dict first to avoid logic errors where "repeated_letters" is treated as literal text rather than data structure evaluation:
            
            print("Repeated Letters Found:")
            for letter in sorted(r.keys()):
                count = r[letter]
                # Ensure we handle the case correctly without relying on substring containment within sample string itself to verify existence of result, 
                # though typically checking len() is sufficient as per requirements to identify repeated letters:

                print(f"  Letter '{letter}': {count} occurrence(s)")
            
            if not r:
                print("  No repeated letters found.")

if __name__ == '__main__':
    main()