def count_vowels(string_list):
    """
    Accepts a list of strings and returns a dictionary where:
      - keys are the input strings (preserving duplicates if any)
      - values are the counts of vowels in each string.

    Vowels considered: 'a', 'e', 'i', 'o', 'u' (case-insensitive).

    :param string_list: list[str] - Input list of strings.
    :return: dict[str, int] - Dictionary mapping strings to vowel counts.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    result_dict = {}
    
    for s in string_list:
        count = 0
        if isinstance(s, str):
            upper_s = s.lower()
            # Iterate only over alphabetic characters to avoid counting other chars as vowels inadvertently (though strictly set membership handles non-alpha fine too)
            c_iter = iter(upper_s)
            for char in c_iter:
                if char in vowels:
                    count += 1
        
        result_dict[s] = count
    
    return result_dict

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "World!",
        "AEIOU",
        "",
        "rhythm",
        "aeiou"
    ]
    
    vowel_counts_dict = count_vowels(sample_strings)
    print(vowel_counts_dict)