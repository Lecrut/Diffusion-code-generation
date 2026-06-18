def count_vowels(strings):
    """
    Accepts a list of strings and returns a dictionary where keys 
    are the input strings and values are their respective vowel counts.
    
    Args:
        strings (list[str]): List of input string items
        
    Returns:
        dict: Dictionary mapping each string to its vowel count
    """
    vowels = set('aeiouAEIOU')
    result = {}
    for s in strings:
        count = sum(1 for char in s if char in vowels)
        result[s] = count
    return result

if __name__ == '__main__':
    sample_strings = ["hello", "world", "aeiou", "Python"]
    vowel_counts = count_vowels(sample_strings)
    print(vowel_counts)