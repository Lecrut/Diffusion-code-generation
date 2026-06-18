def count_vowels(string_list):
    """
    Accepts a list of strings and returns a dictionary where keys are 
    the input strings and values are their respective vowel counts (case-insensitive).
    
    Args:
        string_list (list[str]): A list of strings to process.
        
    Returns:
        dict: Dictionary mapping each string to its vowel count.
    """
    vowels = set("aeiouAEIOU")
    result_dict = {}

    for item in string_list:
        if isinstance(item, str):
            # Count occurrences of any vowel character (case-insensitive)
            count = sum(1 for char in item if char.lower() in "aeiou")
            result_dict[item] = count
        else:
            raise TypeError(f"Expected a string, got {type(item).__name__}")

    return result_dict

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    sample_strings = ["hello", "world", "aeiou", "AEIOU", "", "rhythm"]
    
    output_dictionary = count_vowels(sample_strings)

    print("Input List:", sample_strings)
    print("\nOutput Dictionary:")
    for key, value in output_dictionary.items():
        print(f"'{key}': {value}")