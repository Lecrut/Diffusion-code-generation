import re

def find_nested_substrings(phrase: str) -> list[list[str]]:
    """
    Finds all nested substrings within a given phrase, handling overlapping cases correctly.
    
    A 'nested substring' is defined here as any contiguous sequence of characters 
    that starts and ends with the same character (e.g., "aba", "aaaa"), including single-character strings.
    This definition naturally handles overlaps because every valid start-end pair within a larger string 
    generates its own set of nested substrings if we consider all possible inner layers, 
    but to keep it efficient and aligned with typical 'nested' patterns in text analysis:
    
    We interpret "all nested substrings" as the complete set of palindromic-like structures (start==end)
    at every nesting level. However, a more robust interpretation for general phrases without assuming palindrome logic 
    is simply to find all contiguous substrings where start_index == end_index in terms of character value? No, that's trivial.
    
    Let's re-read the prompt carefully: "find all nested substrings within a phrase". In computer science, 
    "nested" often implies containment or recursion. But without specific constraints like palindromes, 
    it usually means finding patterns where one substring is contained inside another at different levels?
    
    Given the ambiguity and lack of example data in the prompt (only code), I will implement a solution that finds:
    1. All substrings `s[i:j]` such that s[i] == s[j-1]. This creates a "nested" look-alike structure 
       where boundaries match, often resembling palindromic prefixes/suffixes or symmetric patterns.
    2. For each matching pair (i, j), we generate all substrings within the range [i+1 : j-1] recursively if possible?
    
    Actually, to ensure efficiency and correctness with overlaps:
    We will identify every substring where the first character equals the last character. 
    Then, for those that have a non-empty inner part (length > 3), we treat their inner parts as potentially nested layers themselves.
    
    However, a simpler and highly efficient interpretation often used in such puzzles is finding all substrings `s[start:end]` where s[start] == s[end-1]. 
    We will collect these, ensuring overlaps are counted separately for each valid pair found.
    
    Algorithm:
    1. Iterate through every possible start index i from 0 to len(phrase)-2.
    2. For each i, iterate j (end) from i+2 to len(phrase). 
       Why i+2? Because we want at least one character inside if nesting implies depth > 0? Or maybe even length >= 1 is allowed for "nested"?
       Let's assume minimum length of the substring itself must be 3 to have an inner layer, or just check start==end char.
       
    Decision: We will find all substrings s[i:j] where phrase[i] == phrase[j-1]. 
    If a substring has length L >= 2 and starts/ends with same char, it qualifies as a "nested" candidate in this context (symmetric boundaries).
    
    To handle the word "efficiently": O(N^2) is acceptable for string processing unless N is huge. Given no performance constraints on N specifically other than efficiency relative to brute force enumeration of all substrings, 
    we stick with direct iteration which avoids complex data structures like suffix trees unless necessary (which would be overkill and hard to explain without examples).
    
    Refinement: "Nested" might imply recursive containment? e.g. "ababa": "a...a", then inside is "bab". Inside that "b...b". 
    So we want layers.
    
    Let's implement a function `get_nested_layers` which returns all substrings s[i:j] such that phrase[i]==phrase[j-1].
    We will also include single characters if the definition allows, but typically "nested" implies structure around an inner core.
    To be safe and comprehensive: Include any substring where start char == end char. 
    If length > 3 (so there is something inside), we can optionally recurse? No, just listing all such substrings forms a set of nested structures.
    
    Actually, let's look at the phrasing "return them in a structured list". 
    Let's return a list where each element is a tuple: [outer_substring, inner_substrings].
    If no inner strings exist (length 2 or start/end match but nothing inside), just include the outer.
    
    Wait, simpler interpretation often used in coding challenges for "nested substrings" without specific rules like palindromes is simply finding all contiguous segments where boundaries are identical characters. 
    We will implement this: Find every substring s[i:j] (inclusive i, exclusive j) such that phrase[i] == phrase[j-1].
    
    Let's refine the definition to be extremely clear for the user via comments in code:
    "Nested Substring": A contiguous substring `phrase[start:end]` where `phrase[start] == phrase[end-1]`. 
    This creates a 'nested' appearance (like brackets < ... >). We will collect all such substrings.
    
    Efficiency Note: O(N^2) to check every pair, which is optimal for arbitrary pattern matching without advanced structures given the output requirement of listing them all explicitly anyway.
"""

def find_all_nested_substrings(text: str):
    """
    Finds all contiguous substrings where the first and last characters are identical.
    
    Args:
        text (str): The input phrase to analyze.
        
    Returns:
        list[list[str]]: A structured list of lists, where each inner list contains 
                         [full_substring, start_index, end_index].
                         
    Examples:
        Input: "aba" -> ["ab", 0, 1] (wait, a==b? No. 'a'=='a'? Yes at indices 0 and 2)
               Result for "aba": 
                 - Substring s[0:3] ("aba"): start='a', end='a'. Inner is "ba"? Or just the string itself?
                 Let's return [substring, length].
    """
    result = []
    
    n = len(text)
    
    # Iterate over all possible starting positions and ending positions
    for i in range(n):
        char_start = text[i]
        
        # We need at least one character after start to form a substring of length >= 1? 
        # Actually, the prompt says "nested", which implies structure. 
        # Let's assume we want substrings where boundaries match and there is potentially content inside OR it's just two matching chars.
        # To be strictly efficient and correct for overlaps: check every j > i+1 to ensure something 'inside' exists? Or include length 2?
        # If I take "aa", start=a, end=a. Is it nested? Yes, boundaries match.
        
        for j in range(i + 1, n):
            if text[j] == char_start:
                substring = text[i:j+1] # inclusive slicing [i : j+1] -> indices i and j are the ends
                
                # Store result as a dictionary-like structure or list of lists per instruction "structured list"
                # Let's use a list containing (substring, start_index, end_index) to be clear.
                result.append([substring, i, j])
                
    return result

if __name__ == '__main__':
    sample_phrases = [
        "abacaba",      # Classic palindrome with many nested matches
        "hello world",  # No matching boundary chars except maybe if 'l' appears twice? h...o, e...r, l...d. None match boundaries exactly in whole word unless specific pattern exists like "level" -> l..v (no), l..e(no). Wait: level -> l==l. So yes.)
        "ababa",         # Multiple nested layers of 'a' and 'b'
        "",              # Edge case empty string
    ]

    for phrase in sample_phrases:
        print(f"Phrase: '{phrase}'")
        substrings = find_all_nested_substrings(phrase)
        
        formatted_output = []
        for item in substrings:
            s, start, end = item[0], int(item[1]), int(item[2]) if len(item) > 2 else None
            # Ensure we handle the list structure correctly as per return requirement
            # The function returns a flat list of lists. 
            formatted_output.append(f"Index [{start}:{end}]: '{s}' (Chars: {s.startswith('a') or s.endswith('b')}?)") 
            
        print("Nested Substrings found:")