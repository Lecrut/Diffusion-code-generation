def find_palindromes(text):
    words = text.lower().split()
    palindromes = [word for word in words if word == word[::-1] and len(word) > 1]
    return sorted(list(set(palindromes)))

if __name__ == '__main__':
    sample_text = "Madam Arora teaches malayalam. A man a plan a canal Panama."
    result = find_palindromes(sample_text)
    print(result)