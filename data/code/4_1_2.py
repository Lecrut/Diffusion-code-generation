import re

def count_consonants(word):
    if not isinstance(word, str):
        return 0
    cleaned_word = re.sub(r'[^a-zA-Z]', '', word)
    vowels = set('aeiouAEIOU')
    count = 0
    for char in cleaned_word:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

if __name__ == '__main__':
    test_cases = [
        "Hello, World!",
        "Python3.11",
        "Schrödinger's cat",
        "12345",
        "AEIOUaeiou",
        "bcdfgBCDFG",
        "",
        "!!!",
        "A b c D e F g H i J k L m N o P q R s T u V w X y Z"
    ]
    for case in test_cases:
        result = count_consonants(case)
        print(f"Input: '{case}' -> Consonants: {result}")