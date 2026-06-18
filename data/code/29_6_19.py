import sys

def reverse_word(word):
    """Returns the reversed version of the input word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user interaction)
    test_cases = ["hello", "Python", ""]

    for word in test_cases:
        result = reverse_word(word)
        print(result)