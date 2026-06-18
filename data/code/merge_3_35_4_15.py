def count_vowels(strings):
    """
    Accepts a list of strings and returns a dictionary where keys are 
    the input strings and values are their respective vowel counts (case-insensitive).
    
    Args:
        strings (list[str]): List of input strings.
        
    Returns:
        dict: Mapping of string to its vowel count.
    """
    vowels = set("aeiouAEIOU")
    result = {}
    
    for s in strings:
        count = sum(1 for char in s if char in vowels)
        result[s] = count
        
    return result

if __name__ == '__main__':
    sample_data = [
        "hello",
        "world",
        "aeiou",
        "",
        "AEIOU"
    ]
    
    output = count_vowels(sample_data)
    print(output)