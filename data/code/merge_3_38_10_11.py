import string

def find_repeated_letters(text: str) -> dict[str, int]:
    """
    Counts occurrences of each letter in the input text (case-insensitive),
    ignoring non-alphabetic characters and whitespace. Returns a dictionary
    mapping letters that appear more than once to their counts.

    Args:
        text (str): The input string to analyze.

    Returns:
        dict[str, int]: A dictionary where keys are repeated lowercase letters
                        and values are the number of times they appeared in total.
    """
    cleaned_text = ''.join(char.lower() for char in text if char.isalpha())
    
    letter_counts = {}
    for char in cleaned_text:
        letter_counts[char] = letter_counts.get(char, 0) + 1
    
    repeated_letters = {k: v for k, v in letter_counts.items() if v > 1}
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    samples = [
        "Hello World",          # Expected: h -> 2, l -> 3 (case insensitive 'h')
        "Python Programming",   # Expected: p -> 2, r -> 2, o -> 2
        "The quick brown fox jumps over the lazy dog"  # No repeated letters in standard pangram case? 
                                                                    # Actually 't', 'e' repeat. Let's verify manually for sample below logic.
    ]

    print("Repeated Letters Analysis\n")
    
    for i, test_str in enumerate(samples, 1):
        result = find_repeated_letters(test_str)
        
        if not result:
            print(f"Sample {i}: '{test_str}'")
            print("Result: No repeated letters found.\n")
        else:
            # Sort keys for consistent output order (e.g., alphabetical by letter index or just insertion sort stability isn't guaranteed, so sorting)
            sorted_result = dict(sorted(result.items()))
            
            print(f"Sample {i}: '{test_str}'")
            repeated_list = list(repeated_letters.keys())
            if len(repeated_list) == 1:
                char_count = result[sorted_result[list(repeated_list)[0]]]
                print(f"Repeated letter(s): '{repeated_list[0].upper()}' (appearing {char_count} times)")
            else:
                for char, count in sorted_result.items():
                    print(f"- Letter '{char.upper()}' appears {count} time(s)")
            print("-" * 40)