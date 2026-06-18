import re

def find_pattern_matches(text: str, patterns: list) -> dict:
    """
    Takes a string and a list of regex patterns.
    Returns a dictionary mapping each pattern to a list of all non-overlapping 
    substrings in the input text that match it.

    Args:
        text (str): The input string to search within.
        patterns (list[str]): A list of regular expression strings.

    Returns:
        dict: Keys are the original pattern strings, values are lists of matched substrings.
              If a pattern matches multiple times in overlapping regions, 
              only non-overlapping occurrences from left-to-right scanning per pattern instance 
              is considered here for simplicity; however, since patterns can match different parts 
              simultaneously (e.g., 'a' and 'ab'), we collect all matches independently for each pattern.
    """
    results = {}

    # Compile regex flags to handle case-insensitivity if needed or specific needs later.
    # For this utility, no special global flag is set unless specified in the problem context; 
    # standard matching behavior applies (case-sensitive by default).
    
    for pattern_str in patterns:
        try:
            compiled_pattern = re.compile(pattern_str)
        except re.error as e:
            results[pattern_str] = []  # Store empty list if regex is invalid to avoid crashing silently
            
        matches = []
        
        # Find all non-overlapping matches for this specific pattern in the text.
        # Using finditer allows us to capture the actual matched string, not just indices.
        for match in compiled_pattern.finditer(text):
            matches.append(match.group())
            
        results[pattern_str] = matches

    return results

if __name__ == '__main__':
    sample_text = "The rain in Spain stays mainly in the plain"
    
    # Sample patterns to test: 
    # 1. Simple substring match ('ain')
    # 2. Word boundary or specific word structure (e.g., 'Spain' exact)
    # 3. Regex pattern for vowels at start of words if we wanted, but let's keep it simple with regex syntax
    
    sample_patterns = [
        "ain",           # Matches any occurrence of the substring "ain"
        r"\bRain\b",     # Case-sensitive word match (will not find 'rain' in lowercase unless text matches) 
                        # Note: The input text has 'The rain...', so this specific pattern might fail case-sensitively.
                        # Let's adjust to a more robust test or just use the literal string for demonstration of logic.
        "ain",           # Duplicate to show same result, or let's change one to be distinct like "\bRain\b" vs "rain"
    ]

    # Corrected sample patterns based on case sensitivity in 'The rain...'
    final_patterns = [
        r"\w+in\w+",     # Matches words ending with 'in' (e.g., Spain, plain) - wait, regex logic check: \w matches letters/digits/underscore. 
                        # "Spain" ends with 'ain', not just 'n'. Let's stick to simple substring or clear word match.
        r"\bRain\b",      # This won't match because text is lowercase 'rain'. Let's use a pattern that definitely works: \w+in\w*? No, let's simplify.
    ]

    # Refined sample patterns for guaranteed matches in "The rain in Spain stays mainly in the plain"
    refined_patterns = [
        r"in",            # Matches 'in' (e.g., 'rain', 'in', 'plain') - wait, 'ain' contains 'an'. 
                         # Actually, let's use specific substrings.
        "ain",           # Matches 'ain' in rain, Spain, mainly, plain.
    ]

    # Let's create a more diverse set of patterns for the sample text to demonstrate functionality well.
    test_patterns = [
        r"in",            # Should match: rain(in), in(in), plain(in) -> actually "rain" has 'in', "Spain" no, "plain" yes? 
                         # Wait: S-p-a-i-n. No 'i' followed by 'n'? Yes it does (ai-n). So Spain matches r"in".
                         # Let's re-verify text: "The rain in Spain stays mainly in the plain"
                         # Matches for "in": "rain", "in", "plain"? 
                         # "Spain": S-p-a-i-n. Contains 'i' then 'n'. Yes.
        r"\bRain\b",      # Won't match due to case sensitivity unless text was capitalized differently or we use re.IGNORECASE.
                        # To ensure robustness without changing input, let's avoid strict word boundaries if case differs significantly 
                        # OR assume the user handles flags. Let's stick to simple string inclusion for safety in this demo context.
    ]

    # Final decision: Use patterns that are guaranteed to match given standard regex rules (case-sensitive).
    sample_patterns_final = [
        r"in",            # Matches 'in' inside rain, Spain(in), plain? 
                         # "Spain": ...i-n... Yes.
                         # "plain": p-l-a-i-n -> i then n. Yes.
                         # So matches: 'rain', 'in', 'Spain', 'stays'(no), 'mainly'(m-a-i-n->yes, but pattern is just in? No, r"in" means literal string 'in').
        "ain",            # Matches 'ain' inside rain, Spain(ain?), mainly(ain?). 
                         # "rain": r-a-i-n -> contains ain. Yes.
                         # "Spain": S-p-a-i-n -> a-i-n? No, it's p-a-i-n (no 'a' before i). Wait: S-p-**ai**-n. It has 'i', then 'n'. Does it have 'ain'? 
                         # Indices in Spain: 0:S, 1:p, 2:a, 3:i, 4:n. Substring at 2 is "ain". Yes.
                         # "mainly": m-a-i-n-l-y. Contains "ain" (indices a,i,n). Yes.
    ]

    print(find_pattern_matches(sample_text, sample_patterns_final))