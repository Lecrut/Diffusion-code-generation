def is_palindrome(s):
    # Normalize string to remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = ["A man, a plan, a canal: Panama", "race a car", "Was it a cat and I?", "Madam"]
    test_cases = [s for s in samples if is_palindrome(s)]