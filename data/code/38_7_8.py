def find_duplicate_letters(text: str) -> list[str]:
    """
    Returns a sorted list of unique letters that appear at least twice in the input string,
    treating uppercase and lowercase versions as the same letter. Non-alphabetic characters are ignored.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        List[str]: A sorted list of lower-case unique letters that appear at least twice.
    """
    # Dictionary to count occurrences of each lowercase letter
    char_count = {}
    
    for char in text.lower():
        if 'a' <= char <= 'z':  # Only consider alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1
            
    result = []
    seen_letters = set()
    
    # Collect letters that appear more than once and ensure uniqueness in the output list
    for letter, count in char_count.items():
        if count > 1:
            if letter not in seen_letters:
                result.append(letter)
                seen_letters.add(letter)
                
    return sorted(result)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or files needed)
    test_strings = [
        "Hello World!",      # Expected: ['e', 'h'] -> actually 'l' appears 3 times, so ['e','l'], but let's trace: h=1,e=2,l=4,o=2,w=1,r=1,d=1. So unique duplicates: e, l, o
        "A man a plan",      # Expected: ['a', 'm'] -> A,a,m,n,p,l,a,n -> counts: a=3, m=2, n=2, p=1, l=1. Duplicates: a, m, n
        "Programming in Python", 
    ]

    for test_str in test_strings:
        duplicates = find_duplicate_letters(test_str)
        print(f"Input: '{test_str}'")
        print(f"Duplicate letters: {duplicates}")
        print("-" * 20)