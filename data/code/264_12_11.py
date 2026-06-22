def find_all_palindromes(text):
    words = text.lower().split()
    palindromes = [word for word in words if word == word[::-1] and len(word) > 1]
    return sorted(palindromes)

if __name__ == '__main__':
    sample_text = "Able was I ere I saw Elba. Madam, In Eden, I'm Adam."
    result = find_all_palindromes(sample_text)
    print(result)