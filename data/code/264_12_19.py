def find_palindromes(text):
    words = text.split()
    palindromes = [word for word in words if word == word[::-1] and len(word) > 1]
    return palindromes

if __name__ == '__main__':
    sample_text = "Madam Arora teaches malayalam"
    print(find_palindromes(sample_text))