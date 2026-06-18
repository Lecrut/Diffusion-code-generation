def is_palindrome(s: str) -> bool:
    return s == "".join(reversed(s))

if __name__ == "__main__":
    test_strings = ["racecar", "hello123world", "a"]
    for val in test_strings:
        print(val, "->", is_palindrome(val), "|", end=" ")