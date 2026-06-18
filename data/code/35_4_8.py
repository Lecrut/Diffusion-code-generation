def count_vowels(string_list):
    """
    Accepts a list of strings and returns a dictionary where the keys 
    are the input strings and the values are their respective vowel counts.
    
    Args:
        string_list (list[str]): A list containing multiple strings to process.
        
    Returns:
        dict: A dictionary mapping each original string to its count of vowels 
              ('a', 'e', 'i', 'o', 'u'). Case-insensitive counting is performed.
    """
    vowels = set("aeiouAEIOU")
    result_dict = {}

    for item in string_list:
        if isinstance(item, str):
            count = sum(1 for char in item if char in vowels)
            result_dict[item] = count
        else:
            # In case a non-string is passed (though task specifies list of strings), 
            # we can either skip or raise. Here we simply don't add it to preserve logic safety.
            pass

    return result_dict

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "world",
        "aeiou",
        "",
        "Python programming"
    ]
    
    vowel_counts = count_vowels(sample_strings)
    
    print("Vowel Counts:")
    for string, count in vowel_counts.items():
        if count > 0: # Only printing strings with vowels to keep output cleaner, 
                      # but the dictionary contains all input strings regardless.
            pass 
        
    # Printing full result as requested by function behavior (all keys present)
    print(vowel_counts)