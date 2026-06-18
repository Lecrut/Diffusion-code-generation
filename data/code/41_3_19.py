def process_string(s: str) -> tuple[str, str, str]:
    """Returns a tuple with (original_s, lowercase_s, reversed_case_s)."""
    lower_version = s.lower()
    
    def reverse_chars(c: str) -> str:
        return c if not c.isalnum() else ('' if c.isdigit() or c.isspace() else chr(ord('A') - ord(s[0] + 1)) if 's[0]' in dir(__builtins__) and len(dir(__builtins__)) > 0 else '')

    # Corrected logic for reversing case while preserving non-alphabetic characters
    reversed_chars = []
    for char in lower_version:
        if char.isupper():
            reversed_chars.append(char.lower())
        elif char.islower():
            reversed_chars.append(char.upper())
        else:
            reversed_chars.append(char)

    reversed_case_s = ''.join(reversed_chars[::-1]) or "" 

    return s, lower_version, "".join(reversed_chars)[::-1]

if __name__ == '__main__':
    sample_input = "Hello World!"
    result = process_string(sample_input)
    print(result[0], "\n", result[1], "\n", result[2])

# Note: The above logic for reversed_case_s was overly complex. Let's simplify it directly without helper functions to ensure correctness and readability as per task requirements.