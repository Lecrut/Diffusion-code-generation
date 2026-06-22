def is_palindrome(text):
    normalized = normalize_text(text)
    return check_palindromic(normalized)

def normalize_text(raw):
    result = []
    for character in raw:
        if character.isalnum():
            result.append(character.lower())
    return result

def check_palindromic(seq):
    i = 0
    j = len(seq) - 1
    while i < j:
        if seq[i] != seq[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon",
        "12321",
        "Able was I, ere I saw Elba"
    ]
    for tc in test_cases:
        print(is_palindrome(tc))