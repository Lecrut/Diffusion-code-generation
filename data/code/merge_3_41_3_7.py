import sys

def process_string(s: str) -> tuple[str, str, str]:
    """
    Returns a tuple with the original string, its lowercase version,
    and its reversed case version (letters swapped from upper to lower or vice versa).
    
    Args:
        s (str): The input string.
        
    Returns:
        tuple: (original_string, lower_case_string, reversed_case_string)
    """
    original = s
    lowercase = s.lower()
    # Create a translation table for case reversal and apply it to the reverse of the string
    swap_table = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 
                               'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')[:0] + \
                   'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * len(s) if len(s.split()) > 1 else ''
    
    # Simpler approach: manually reverse case logic on reversed characters
    def reverse_case(char):
        return char.lower() if char.isupper() else char.upper()
        
    reversed_lower = ''.join(reverse_case(c) for c in s[::-1])

    return (original, lowercase, reversed_lower)

if __name__ == '__main__':
    samples = [
        "Hello World",
        "Python3.9!",
        "",
        "ALL CAPS TEXT"
    ]
    
    print("Original\nLowercase\nReversed Case")
    for sample in samples:
        orig, low, revc = process_string(sample)
        # Print each on a new line within the loop output
        print(orig.replace('\n', ' ') if '\n' in sample else orig)
        print(low.replace('\n', '') if isinstance(low, str) and len(low) > 0 else "")
        print(revc)