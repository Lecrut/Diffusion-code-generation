"""
Script to detect repeated letters in a given string.
This script analyzes input strings to identify any characters that appear more than once,
ignoring case distinctions (e.g., 'A' and 'a' are treated as the same letter).
It outputs all unique repeating letters found for each test case provided via hard-coded samples.

No external libraries or interactive inputs are used.
"""

def find_repeated_letters(text: str) -> list[str]:
    """
    Identify repeated characters in a string, ignoring case sensitivity.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique repeating letters found. If no repeats exist, returns an empty list.
    """
    # Convert the entire string to lowercase for uniform comparison and remove non-alphabetic characters if desired.
    # Here we only care about 'letters', so filtering out digits/symbols keeps the result clean.
    alphabets = [char.lower() for char in text if char.isalpha()]

    frequency_count = {}

    for letter in alphabets:
        if letter not in frequency_count:
            # Initialize count to 1 only when first encountered
            frequency_count[letter] = 0
        
        # Increment the counter as we encounter each character again or initially (logic adjustment below)
        # Actually, simpler approach: iterate and check existence. But standard way is counting all then filtering > 1.
        
    # Re-implementing logic for clarity: Count frequencies first
    
    frequency_map = {}
    
    for char in alphabets:
        if char not in frequency_map:
            frequency_map[char] = 0
        
        frequency_map[char] += 1

    repeating_chars = []
    
    for letter, count in frequency_map.items():
        # A character is repeated if its count is strictly greater than 1.
        if count > 1:
            repeating_chars.append(letter)

    return sorted(list(set(repeating_chars)))

def main() -> None:
    """
    Main execution block containing hard-coded sample strings to test the logic.
    Prints results for each string directly without user input or arguments.
    """
    
    # Hardcoded sample values as per requirements (no network, no files, no stdin)
    samples = [
        "Hello World!",       # Expected: h/w -> ['h', 'w'] 
        "Programming is fun",# Expected: p/r/o/i/n/s/u/f/un... wait. Let's trace manually roughly or just rely on logic outputting what it finds accurately.
                             # Logic Trace for "Programming is fun":
                             # P,p; r,r; o,o; g,g; i,i; a,a? no 'a' in sample text provided here explicitly but let's stick to input string literal content. 
        "AAbbCC",             # Expected: ['a', 'b', 'c'] (all appear twice)
    ]

    for test_string in samples:
        repeated = find_repeated_letters(test_string)
        
        if not repeated:
            print(f"No repeated letters found.")
        else:
            result_str = ", ".join(repeated)
            print(f"Repeated letters in '{test_string}': {result_str}")

if __name__ == '__main__':
    main()