import sys

def find_repeated_chars(text: str) -> dict[str, int]:
    """
    Detects all repeated characters in the input string using a dictionary to count occurrences.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        dict: A dictionary where keys are characters that appear more than once and values 
              represent their frequency counts. Only includes characters with a count > 1.
              
    Example:
        >>> find_repeated_chars("abracadabra")
        {'a': 5, 'b': 2, 'r': 2}
    """
    char_count = {}
    
    # Iterate over each character in the string and update its count
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    # Filter to keep only characters that appear more than once (repeated)
    repeated_chars = {char: count for char, count in char_count.items() if count > 1}
    
    return repeated_chars

def main():
    """
    Main execution block with hard-coded sample values.
    Runs without user input or external dependencies.
    """
    # Sample inputs to test the function with various cases including uppercase and lowercase
    samples = [
        "hello world",               # Basic case: l, o appear twice (or thrice depending on space handling)
        "abracadabra",              # Classic anagram for 'a' being repeated heavily
        "Python is awesome!",       # Mixed case test
        ""                          # Edge case: empty string
    ]
    
    print("Repeated Character Detector")
    print("=" * 30)
    
    for sample in samples:
        print(f"\nInput: '{sample}'")
        
        if not sample:
            print("No repeated characters found (empty input).")
            continue
            
        result = find_repeated_chars(sample)
        
        if not result:
            print("No repeated characters found.")
        else:
            # Sort the items by character for consistent output order
            sorted_result = dict(sorted(result.items()))
            
            char_list = list(sorted_result.keys())
            counts = [sorted_result[c] for c in char_list]
            
            if len(char_list) == 1 and all(c == count[0] for c, count in result.items()):
                # Special format for single repeated character type like 'a' appearing multiple times
                print(f"Repeated Character: '{char_list[0]} ({counts[0]} occurrences)'")
            else:
                formatted_parts = []
                for char, count in sorted_result.items():
                    formatted_parts.append(f"'{char}': {count}")
                
                # Create a clear string representation of the repeated characters and their counts
                parts_str = " ".join(formatted_parts)
                print(parts_str)

if __name__ == '__main__':
    main()