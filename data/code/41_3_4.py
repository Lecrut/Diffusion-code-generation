def process_string(s: str) -> tuple[str, str, str]:
    """Returns a tuple with the original string, its lowercase version, 
    and its reversed case version."""
    lowercased = s.lower()
    
    # Reverse each character's case if it is alphabetic (a->A, A->a), otherwise keep as is.
    def reverse_case(char: str) -> str:
        return char.swapcase() if char.isalpha() else char
    
    reversed_cased_str = "".join(reverse_case(c) for c in s[::-1])
    
    return (s, lowercased, reversed_cased_str)

if __name__ == '__main__':
    sample_input = "Hello World!"
    result = process_string(sample_input)
    original, lowercase, reversed_version = result
    
    # Print results to verify functionality without user interaction
    print("Original:", original)
    print("Lowercase:", lowercase)
    print("Reversed Case:", reversed_version)