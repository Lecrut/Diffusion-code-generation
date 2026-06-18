def process_string(input_str):
    """
    Accepts a string and returns a tuple with:
    - The original string
    - Its lowercase version
    - Its reversed case version (characters swapped in order, then lowercased)
    
    Note: 'reversed case' is interpreted as reversing the character sequence.
    If the requirement meant swapping cases (uppercase to lowercase and vice versa),
    that would be a different operation. Given "reversed", string reversal is assumed.
    """
    original = input_str
    lowercased = input_str.lower()
    reversed_string = input_str[::-1]  # Python slicing for reverse
    
    return (original, lowercased, reversed_string)

if __name__ == '__main__':
    sample_input = "Hello World!"
    
    result = process_string(sample_input)
    
    print(f"Original: {result[0]}")
    print(f"Lowercase: {result[1]}")
    print(f"Reversed: {result[2]}")