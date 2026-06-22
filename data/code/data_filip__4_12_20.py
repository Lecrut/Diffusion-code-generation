import re

def count_consonants(text: str) -> int:
    vowels = "aeiouAEIOU"
    letters_only = re.sub(r'[^a-zA-Z]', '', text)
    consonants = [char for char in letters_only if char not in vowels]
    return len(consonants)

if __name__ == '__main__':
    test_string = "Hello, World! 123 Programming is fun & efficient."
    result = count_consonants(test_string)
    print(result)