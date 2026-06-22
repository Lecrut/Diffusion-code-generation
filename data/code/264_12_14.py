def find_palindromic_words(text):
    words = text.lower().split()
    palindrome_dict = {word: word == word[::-1] for word in words}
    palindromes = [word for word, is_palindrome in palindrome_dict.items() if is_palindrome]
    return sorted(list(set(palindromes)))

if __name__ == '__main__':
    sample_text = "Madam Arora teaches malayalam"
    result = find_palindromic_words(sample_text)
    print(result)