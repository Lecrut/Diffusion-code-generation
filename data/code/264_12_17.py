def is_palindrome(word):
    return word == word[::-1]

def find_all_palindromes(text):
    words = text.lower().split()
    palindromes = [word for word in words if is_palindrome(word)]
    return sorted(list(set(palindromes)))

if __name__ == '__main__':
    sample_text = "Madam Arora teaches malayalam. A man a plan a canal Panama."
    result = find_all_palindromes(sample_text)
    print(result)