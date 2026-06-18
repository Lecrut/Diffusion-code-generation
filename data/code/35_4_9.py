def count_vowels(string_list):
    """
    Accepts a list of strings and returns a dictionary where keys 
    are the input strings and values are their respective vowel counts.
    
    Args:
        string_list (list[str]): List of input strings
        
    Returns:
        dict: Dictionary mapping each string to its vowel count
    """
    vowels = set("aeiouAEIOU")
    result_dict = {}
    
    for item in string_list:
        if isinstance(item, str):
            count = sum(1 for char in item if char in vowels)
            result_dict[item] = count
    
    return result_dict

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    sample_strings = ["hello", "world", "aeiou", "AEIOU", "", "rhythm"]
    
    vowel_counts = count_vowels(sample_strings)
    
    print("Vowel counts:", vowel_counts)