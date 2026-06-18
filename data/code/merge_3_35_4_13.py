def count_vowels(input_strings):
    """
    Accepts a list of strings and returns a dictionary where keys 
    are the input strings and values are their respective vowel counts (case-insensitive).
    
    Vowels considered: 'a', 'e', 'i', 'o', 'u'
    """
    vowels = set('aeiouAEIOU')
    result_dict = {}

    for string in input_strings:
        # Ensure we handle non-string inputs gracefully by treating them as empty or skipping if not str,
        # though the problem implies a list of strings. We'll assume valid string input per spec.
        vowel_count = sum(1 for char in string.lower() if char in vowels)
        result_dict[string] = vowel_count

    return result_dict

if __name__ == '__main__':
    sample_data = ["Hello", "World!", "AEIOU", "", "Python Programming"]
    output_result = count_vowels(sample_data)
    
    # Print the result to console for verification without user interaction
    print(f"Input: {sample_data}")
    print("Output Dictionary:")
    for key, value in output_result.items():
        print(f"{key!r}: {value}")