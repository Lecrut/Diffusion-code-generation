def count_vowels(string_list):
    """
    Accepts a list of strings and returns a dictionary where keys are 
    the input strings and values are their respective vowel counts (case-insensitive).
    
    Args:
        string_list (list of str): List of input strings.
        
    Returns:
        dict: Dictionary mapping each string to its vowel count.
    """
    vowels = set('aeiouAEIOU')
    result_dict = {}

    for item in string_list:
        if isinstance(item, str):
            count = sum(1 for char in item if char in vowels)
            result_dict[item] = count
        else:
            # If a non-string element is present (though task specifies list of strings), 
            # we can choose to skip it or raise an error. Here we skip silently as per typical robustness,
            # but strictly following "list of strings", this case shouldn't occur in valid input.
            pass
            
    return result_dict

if __name__ == '__main__':
    sample_data = ["hello", "world", "aeiou", "", "Python"]

    output_vowels_map = count_vowels(sample_data)

    print("Input List:", sample_data)
    print("\nOutput Dictionary:")
    for key, value in output_vowels_map.items():
        print(f'"{key}": {value}')