def count_vowels(word):
    """Returns an integer representing the number of vowels in a string."""
    return sum(1 for char in word.lower() if char in 'aeiou')

def vowel_counts(input_list):
    """Accepts a list of strings and returns a dictionary with 
       keys as input strings and values as their respective vowel counts.
       
       Args:
           input_list (list[str]): A list containing string elements to analyze.
           
       Returns:
           dict: Mapping each original string to its vowel count.
    """
    return {word: count_vowels(word) for word in input_list}

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, CLI args, or files).
    samples = ["hello", "world", "aeiou", "rhythm"]
    
    result = vowel_counts(samples)
    
    print("Input:", samples)
    print("Vowel Counts:", result)