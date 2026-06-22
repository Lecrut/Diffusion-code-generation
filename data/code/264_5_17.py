PALINDROME_THRESHOLD = 2

def is_palindrome(word):
    return word == word[::-1]

def find_palindromes(text):
    words = text.split()
    palindromes = [word for word in words if is_palindrome(word) and len(word) > PALINDROME_THRESHOLD]
    return palindromes

if __name__ == '__main__':
    sample_text = "madam arora teaches malayalam"
    result = find_palindromes(sample_text)
    print(result)