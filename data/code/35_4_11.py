def count_vowels(strings):
    """
    Accepts a list of strings and returns a dictionary where keys are 
    the input strings and values are their respective vowel counts.
    
    Vowels considered: 'a', 'e', 'i', 'o', 'u' (case-insensitive).
    """
    vowels = set("aeiouAEIOU")
    result = {}
    
    for string in strings:
        count = sum(1 for char in string if char in vowels)
        result[string] = count
        
    return result

if __name__ == '__main__':
    sample_data = ["hello", "world", "aeiou", "rhythm"]
    output = count_vowels(sample_data)
    
    # Print the result to verify functionality without external input
    print(output)