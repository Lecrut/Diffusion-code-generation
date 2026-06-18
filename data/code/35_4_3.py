def count_vowels(strings):
    """
    Accepts a list of strings and returns a dictionary where 
    keys are the input strings and values are their respective vowel counts.
    
    Vowels considered: 'a', 'e', 'i', 'o', 'u' (case-insensitive).
    """
    vowels = set("aeiou")
    result_dict = {}
    
    for string in strings:
        # Count occurrences of lowercase and uppercase vowels separately if case matters,
        # but typically vowel counting is case-insensitive. This implementation counts 
        # all matching characters regardless of case.
        count = 0
        current_string_lower = string.lower()
        
        for char in current_string_lower:
            if char in vowels:
                count += 1
        
        result_dict[string] = count
    
    return result_dict

if __name__ == '__main__':
    sample_strings = ["hello", "world", "aeiou", "RACECAR"]
    
    output_dictionary = count_vowels(sample_strings)
    print(output_dictionary)