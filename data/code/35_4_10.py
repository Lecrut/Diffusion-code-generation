def count_vowels(strings):
    """
    Accepts a list of strings and returns a dictionary where keys 
    are the input strings and values are their respective vowel counts.
    
    Args:
        strings (list[str]): List of input string elements
        
    Returns:
        dict: Dictionary mapping each string to its vowel count
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}  # Using lowercase only for simplicity
    
    result_dict = {}
    
    for s in strings:
        vowel_count = sum(1 for char in s if char.lower() in vowels)
        result_dict[s] = vowel_count
        
    return result_dict

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files, etc.)
    sample_strings = ["hello", "world", "", "aeiou"]
    
    output_dictionary = count_vowels(sample_strings)
    
    print("Input strings:", sample_strings)
    print("\nOutput dictionary:")
    for k, v in output_dictionary.items():
        print(f"  '{k}': {v}")