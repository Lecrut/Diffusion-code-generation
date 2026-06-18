class VowelCounter:
    """A class to count vowels in a given string."""
    
    def __init__(self, text):
        self.text = str(text) if not isinstance(self.text, str) else self.text
    
    def get_vowel_count(self):
        """Returns the total number of vowel characters (a, e, i, o, u) in the string.
        
        Case-insensitive comparison is performed by converting all vowels to lowercase.
        Only alphabetic vowels are counted; non-alphabetic characters like 'y' or numbers 
        do not trigger a count unless specifically defined as vowels here. Based on standard 
        definition: A, E, I, O, U (and their lowercase equivalents)."""
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return sum(1 for char in self.text if char.lower() in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        "Hello World",           # Expected: 3 (e, o, o) -> Actually 'H' is not vowel, so e, o, i? Wait: H-e-llo W-o-rld -> e, o, o = 2 vowels? Let's recheck.
                                # H - no
                                # e - yes (1)
                                # l - no
                                # l - no
                                # o - yes (2)
                                # space - no
                                # W - no
                                # o - yes (3) -> Wait, 'Hello World' has: e, o, o. That's 3? 
                                # H-e-llo-W-o-r-l-d
                                # Vowels at indices 1 ('e'), 4 ('o'), 6 ('o'). Total = 3. Correct.
        "AEIOU",                  # Expected: 5
        "Rhythm",                # Expected: 0 (No standard vowels)
        "Aeolian",               # Expected: 3 (A, e, o - wait 'i' is also there? A-e-o-i-a-n. Yes.) 
                                # A(1), e(2), i(3), a(4). Total = 4. Let's recount manually.
                                # A -> yes
                                # e -> yes
                                # o -> no, wait 'Aeolian' is spelled A-e-o-l-i-a-n? No, Ae-O-li-an. 
                                # Spelling: A - e - o - l - i - a - n ? Actually "Aeolian" usually implies having an O or U sound but spelling varies.
                                # Standard English word "AEOLIAN": A-E-I-A-N (Wait, does it have O? No, Ae-O-li-an comes from Greek). 
                                # Let's stick to the literal string provided in my mind: "Aeolian". 
                                # If I type "Aeolian" into a python shell:
                                # 'a' -> 1
                                # 'e' -> 2
                                # 'o'? No, it is spelled A-e-o-li-a-n? Or just letters.
                                # Let's assume the string literal provided in code is exactly "AEOLIAN" for simplicity or specific word. 
                                # Actually let's use a clearer example: "Beautiful".
        "Beautiful",              # B-e-a-u-t-i-f-u-l -> e, a, u, i, u = 5 vowels.
    ]

    for sample in samples:
        counter = VowelCounter(sample)
        count = counter.get_vowel_count()
        print(f"String: '{sample}'")
        print(f"Vowel Count: {count}")