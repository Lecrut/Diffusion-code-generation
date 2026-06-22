def find_palindromic_words(text):
    words = text.lower().split()
    palindromes = [word for word in words if word == word[::-1] and len(word) > 1]
    return sorted(list(set(palindromes)))

if __name__ == '__main__':
    sample_text = "Madam Arora teaches malayalam. Is it a racecar or a level?"
    result = find_palindromic_words(sample_text)
    print(result)