def is_palindrome(word):
    return word == word[::-1]

def find_all_palindromes(text):
    words = text.lower().split()
    palindrome_words = [word for word in words if is_palindrome(word) and len(word) > 1]
    return sorted(palindrome_words)

if __name__ == '__main__':
    sample_text = "Able was I ere I saw Elba, Madam In Eden, Adam."
    result = find_all_palindromes(sample_text)
    print(result)