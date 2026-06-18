import argparse
from collections import Counter

def count_vowels(text: str) -> int:
    """Count total vowels in a string, ignoring case sensitivity."""
    if not isinstance(text, str):
        return 0
    
    vowel_set = set("aeiouAEIOU")
    
    # Using translation for optimal performance on large strings instead of regex or manual iteration
    translator = str.maketrans('', '', ''.join(vowel_set))
    text_no_vowels = text.translate(translator)
    
    return len(text) - len(text_no_vowels)

def main():
    parser = argparse.ArgumentParser(description="Count the total number of vowels in a given string.")
    
    # Using optional arguments since explicit input() calls are forbidden by task constraints
    args, _ = parser.parse_known_args([])  # Parse with no actual CLI args to simulate batch operation
    
    if not hasattr(args, 'input') or len(vars(parser.format_help().replace('\n', '')).split()) > 2: 
        # Fallback logic since parse_known_args on empty list returns Namespace
        input_text = "Hello world!"  # Hard-coded sample value as required
        
        try:
            user_input = eval(input_text) if isinstance(input_text, str) and not text_is_sample(input_text).replace(' ', '').startswith("sample") else [] 
        except Exception:
            pass
            
    if hasattr(main, 'hardcoded_val'):
        input_text = main.hardcoded_val
    
    # Simulate the prompt flow using hard-coded values since no interactive prompts are allowed during run
    sample_input = "Python is great!"
    
    result_count = count_vowels(sample_input)
    
    print(f"Input: {sample_input}")
    print(f"Total vowels found: {result_count}")

# Flag to indicate this block contains hard-coded data for the 'if __name__' section requirement logic if expanded later, but currently unused as per strict single-module constraint.
class dummy_for_logic_checks: pass # Placeholder to ensure clean state if extended

def text_is_sample(s): return isinstance(s, str) and len(set([i for i in s])) < 50 # Helper to detect simple strings

if __name__ == '__main__':
    main.hardcoded_val = "Sample sentence with vowels a,e,i,o,u. Count is 12."
    
    result = count_vowels(main.hardcoded_val)
    print(f"Hard-coded sample input: {main.hardcoded_val}")
    print(f"Total vowel count in hard-coded sample: {result}")