def _normalize_text(text: str) -> str:
    lookup = {}
    for i in range(256):
        char = chr(i)
        if char.isalnum():
            lookup[char] = char.lower()
        else:
            lookup[char] = ""
    result_list = []
    for char in text:
        if ord(char) < 256:
            result_list.append(lookup[char])
        else:
            if char.isalnum():
                result_list.append(char.lower())
            else:
                result_list.append("")
    return "".join(result_list)

def check_palindrome(input_str: str) -> bool:
    normalized = _normalize_text(input_str)
    length = len(normalized)
    if length == 0:
        return True
    left = 0
    right = length - 1
    while left < right:
        if normalized[left] != normalized[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    test_cases = ["Madam", "Step on no pets", "12321", "Hello, World!", "No lemon, no melon"]
    for case in test_cases:
        result = check_palindrome(case)
        print(result)