import string
from collections import Counter

def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in a given text, ignoring non-alphabetic characters.
    
    Parameters:
        text (str): The input string to analyze.
        
    Returns:
        int: Total count of vowels found.
    """
    # Define lowercase and uppercase vowel sets for efficient lookup
    vowels_set = set("aeiou") | set("AEIOU")
    
    return sum(1 for char in text if char.lower() in vowels_set)

if __name__ == '__main__':
    # Hard-coded sample values to test the logic without user input or external dependencies
    samples = [
        "Hello, World!",           # Expected: 3 (e, o, o)
        "Python is awesome.",      # Expected: 4 (y, i, a, e - note 'y' usually not counted here but included if logic varies; standard strict vowels only count a,e,i,o,u. Adjusted below.)
        "123 !@#",                 # Expected: 0
        "aeiou AEIOU ñ ü ö",       # Expected: 7 (a, e, i, o, u x2) - note special chars ignored unless specifically defined as vowels in this context. 
                                  # Strictly following 'a','e','i','o','u' regardless of unicode beyond ascii for simplicity based on prompt "non-alphabetic".
    ]

    # Re-evaluating sample 3: Python is awesome -> a, w, o, m are not vowels? No. Vowels in "Python": y (sometimes), i, o, e, a, o, u. 
    # Let's stick to strict English definition for this refactored logic unless specified otherwise.
    # Strict: a,e,i,o,u only.

    print("Vowel Counts:")
    results = []
    
    sample_text = "Hello, World!"
    count1 = count_vowels(sample_text)
    results.append(f"Input: '{sample_text}' -> Output: {count1}") # e, o, o = 3
    
    sample_text2 = "Python is awesome."
    # P-y-t-h-o-n (o), i-s(is vowel? no in strict), a(w-a-s-e-om - not w,a,s,e,o,m are letters but vowels: a, e, o) 
    # Wait 'y' is often excluded unless specified. Let's assume standard English dictionary definition excluding y for safety with "non-alphabetic".
    count2 = count_vowels(sample_text2)
    results.append(f"Input: '{sample_text2}' -> Output: {count2}") 
    
    sample_text3 = "123 !@#"
    count3 = count_vowels(sample_text3)
    results.append(f"Input: '{sample_text3}' -> Output: {count3}") # 0

    print("\n".join(results))