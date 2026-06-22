def _normalize(input_str):
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    cleaned = input_str.lower()
    allowed_chars = []
    for char in cleaned:
        if char.isalnum():
            allowed_chars.append(char)
    return "".join(allowed_chars)

def is_palindrome(s):
    normalized = _normalize(s)
    return normalized == normalized[::-1]

if __name__ == '__main__':
    print(is_palindrome("RaceCar"))
    print(is_palindrome("No 'x' in Nixon"))
    print(is_palindrome("Hello"))
    print(is_palindrome("12321"))
    print(is_palindrome("12345"))