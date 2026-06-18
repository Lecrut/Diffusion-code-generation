def count_letter_frequencies(text: str) -> dict[str, int]:
    """Count the frequency of each letter in the input string."""
    freq_map = {}
    
    for char in text:
        # Only consider alphabetic characters (a-z or A-Z), case-insensitive
        if 'a' <= char.lower() <= 'z':
            lower_char = char.lower()
            
            if lower_char in freq_map:
                freq_map[lower_char] += 1
            else:
                freq_map[lower_char] = 0
                
    return dict(freq_map)

def get_frequent_letters(frequency_counts: dict[str, int]) -> list[tuple[str, int]]:
    """Return a sorted list of letters with frequency greater than one."""
    
    # Filter frequencies > 1 and sort alphabetically by letter
    frequent = [(letter, count) for letter, count in frequency_counts.items() if count > 1]
    
    return freq_sort_by_count(frequent)

def freq_sort_by_count(freq_list: list[tuple[str, int]]) -> list[int]:
    """Sort the frequency list by value (frequency), descending."""
    # Sort by frequency first, then alphabetically for ties
    
    frequent_letters = sorted([letter for letter, count in freq_list if count > 1], reverse=True)

    return frequent_letters

def main():
    sample_text = "Hello World! Programming is fun and Python"
    
    frequencies = count_letter_frequencies(sample_text)
    
    result = get_frequent_letters(frequencies)
    
    # Output results
    print("Letter Frequencies:", dict(result))

if __name__ == '__main__':
    main()