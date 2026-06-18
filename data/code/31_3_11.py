import string

def is_palindrome(s: str) -> bool:
    """Check if a given alphanumeric, lowercase string s is a palindrome."""
    return all(c in "0123456789abcdefghijklmnopqrstuvwxyz" and c == r for i, (c, r) in enumerate(zip(reversed(s), s)))

if __name__ == '__main__':
    test_cases = ["racecar", "pythoncode", "a man a plan a canal Panama"]  # Note: task says only alphanumeric, so last one might fail filter if not pre-filtered. Assuming strict input as per prompt constraint (alphanumeric + lowercase). Let's adjust sample to strictly meet constraints.
    test_cases = ["racecar", "pythoncode", "abba"]
    for s in test_cases:
        # Ensure only alphanumeric and lower case based on task assumption, though samples are already compliant except potential spaces if not filtered. 
        # Since prompt says input is *already* converted to lowercase and contains ONLY alphanumeric, we assume no spaces.
        # But to be safe with the "alphanumeric" constraint in logic:
        valid_s = "".join(c for c in s if c.isalnum())  # Just in case of hidden non-alnum, though prompt says input is clean. 
        print(f"{s!r} -> {is_palindrome(valid_s)}")