def reverse_string(text: str) -> str:
    chars = list(text)
    left = 0
    right = len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)

def check_palindrome(text: str) -> bool:
    return text == reverse_string(text)

def run_tests() -> None:
    test_values = ["radar", "hello", "noon", "Python", "civic"]
    for value in test_values:
        result = check_palindrome(value)
        print(result)

if __name__ == '__main__':
    run_tests()