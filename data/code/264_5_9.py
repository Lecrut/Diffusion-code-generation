def is_palindrome(word):
    return word == word[::-1]

def find_palindromes(text):
    words = text.split()
    palindromes = [word for word in words if is_palindrome(word)]
    return palindromes

if __name__ == '__main__':
    SAMPLE_TEXT = "madam arora teaches malayalam"
    result = find_palindromes(SAMPLE_TEXT)
    print(result)