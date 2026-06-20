def _normalize_input(text: str) -> str:
    result = []
    for char in text:
        if char.isalnum():
            result.append(char.lower())
    return ''.join(result)

def is_palindrome(text: str) -> bool:
    normalized = _normalize_input(text)
    length = len(normalized)
    if length == 0:
        return True
    left_index = 0
    right_index = length - 1
    while left_index < right_index:
        if normalized[left_index] != normalized[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True

def run_validation() -> None:
    test_cases = [
        ("Madam, I'm Adam.", True),
        ("Step on no pets.", True),
        ("Hello World", False),
        ("12321", True),
        ("12345", False),
        ("", True),
        ("a", True),
    ]
    for sample, expected in test_cases:
        result = is_palindrome(sample)
        print(f"Input: {sample!r} -> {result} (Expected: {expected})")

if __name__ == '__main__':
    run_validation()