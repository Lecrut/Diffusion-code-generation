def find_palindromes(text):
    words = text.lower().split()
    palindromes = [word for word in words if word == word[::-1]]
    return sorted(palindromes)

if __name__ == '__main__':
    sample_text = "Madam Arora teaches malayalam. Did you notice the level and radar?"
    result = find_palindromes(sample_text)
    print(result)