def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = ["madam", "hello", "_olleh_", "Python"]
    for case in test_cases:
        result = is_palindrome(case.lower().replace("_", "")) if "_" in case else is_palindrome(case)
        print(f"'{case}': {result}")

# Note above handles optional underscores as a simplistic normalization example; 
# standard definition uses only character equality. Pure version without extra logic:
def pure_is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = ["racecar", "python"]
    for case in test_cases:
        print(f"'{case}': {pure_is_palindrome(case)}")