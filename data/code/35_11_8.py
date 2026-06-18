def count_vowels(text: str) -> int:
    """
    Counts the total number of vowel characters in a string, 
    regardless of case or position relative to non-alphabetic characters.

    Args:
        text (str): The input string to analyze.

    Returns:
        int: The count of vowels ('a', 'e', 'i', 'o', 'u') found in the string.
    
    Efficiency Note:
        This function iterates through the string once, checking each character 
        against a set for O(n) time complexity where n is the length of the input string.
        It avoids creating intermediate lists or converting the entire string to lowercase upfront,
        which reduces memory overhead during iteration.
    """
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    
    for char in text:
        if char.lower() in vowels:
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies.
    
    samples = [
        "Hello, World!",          # Expected: 3 (e, o, i) -> actually 'H', 'e', 'o' are vowels? Let's recheck manually. H-e-llo W-o-rld! e,o are there. Wait: e in Hello, o in HellO, o in WoRlD. So 2+1=3? No, H-e-l-L-o (2), W-o-R-l-d (1). Total 3."
        "aeiou",                  # Expected: 5
        "",                      # Expected: 0
        "Python Programming",    # Expected: 4 ('o','a','i','e' -> o in Pytho, a in PrograMming? P-y-t-h-o-n (1), P-r-o-g-r-a-m-m-i-n-g. 'o', 'a', 'i'. Total 3+1=4.)
        "Rhythm",                 # Expected: 2 ('y' is NOT counted based on strict aeiou definition) -> i, y? Standard English vowels usually include Y sometimes but task implies basic set unless specified otherwise. Let's stick to explicit a,e,i,o,u. In R-y-t-h-m, only 'i'? No 'i'. Wait: R-i-t-h-m has an 'y' and no other vowel strictly speaking if we exclude y? Actually standard count often excludes Y. Input "Rhythm" -> i is not there. It's r,y,t,h,m. If strict aeiou then 0? Or maybe I misread the word. Rh-ythm. No vowels in strict sense except maybe 'y' but task says "vowels". Usually means A,E,I,O,U. So count=1 for i if present, else 0. Let's assume standard a,e,i,o,u only.)
        # Correction on samples: 
        # "Hello World": e (yes), o (yes), o (yes). Total 3? H-e-l-l-o W-o-r-l-d. e and two os. Yes 3. Wait, 'y' is not included.
    ]

    for sample in samples:
        result = count_vowels(sample)
        print(f"Input: '{sample}' -> Count of vowels: {result}")