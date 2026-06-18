def count_vowels(text):
    """
    Returns the number of vowels (both uppercase and lowercase) in a given string.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The total count of vowel characters found in the string.
    """
    return sum(1 for char in text if char.lower() in 'aeiou')

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    test_cases = [
        "Hello World",  # Vowels: e, o, o -> 3
        "AEIOU aeiou",  # Vowels: A,E,I,O,U,a,e,i,o,u -> 10
        "",             # No vowels -> 0
        "Rhythm and Rhyme"  # Vowels: i, e, y (often counted as vowel in phonetics but strictly here we check aeiou only), o? 
                          # Let's stick to strict a,e,i,o,u. Rhythm(1:i) + and(2:a,e -> no 'a' is there, wait "and" has a and n d).
                          # Correction: "Rhythm": i (1); "and": a, e (3 letters in word? a-n-d contains 2 vowels if y doesn't count. Standard definition usually includes only A E I O U)
                          # Let's re-evaluate strict list comp target 'aeiou':
                          # Rhyth:m has no vowel except i(1). 
                          # an:d -> a, e are not in "and"? Wait: "a","n","d". Only 'a' is vowel. So 1.
                          # Rhyme: y is typically excluded unless specified. Let's assume strict A E I O U only as per standard programming tasks unless told otherwise. 
                          # Re-reading prompt: "handling both uppercase and lowercase letters". Usually implies a,e,i,o,u. 'y' behavior varies by language spec, let's stick to explicit set {a,e,i,o,u}.
    ]

    for sample in test_cases:
        print(f"Input: '{sample}' -> Vowel count: {count_vowels(sample)}")