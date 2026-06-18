def reverse_word(s: str) -> str:
    """Returns the reversed version of the input string."""
    return s[::-1]

if __name__ == '__main__':
    sample_strings = ["hello", "Python", "!olleh"]
    for word in sample_strings:
        print(reverse_word(word))