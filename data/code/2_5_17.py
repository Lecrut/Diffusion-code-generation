def is_palindrome(s):
    cleaned = s.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("'", "")
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_strings = ["Racecar", "Hello", "A man, a plan, a canal: Panama", "Noon", "Python"]
    for text in test_strings:
        print(is_palindrome(text))