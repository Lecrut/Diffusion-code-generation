def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = [
        "racecar",
        "hello",
        "A man a plan a canal Panama".lower().replace(" ", ""),  # Assuming spaces removed or not present per spec, but keeping logic simple for alphanumeric only input as per assumption. If strict alphanumeric:
        "abcba"
    ]
    
    results = []
    for s in test_cases:
        if all(c.isalnum() and c.islower() for c in s):  # Ensure it meets the precondition of being lowercase alphanumeric (though spec says input is already)
            res = is_palindrome(s)
            print(f"'{s}' -> {res}")
            results.append(res)

    # Example usage without interactive prompts, just printing based on hard-coded values.