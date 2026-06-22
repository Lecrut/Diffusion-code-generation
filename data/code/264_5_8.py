def find_palindromes(text):
    words = text.split()
    return [word for word in words if word == word[::-1]]

if __name__ == '__main__':
    sample_text = "madam arora teaches malayalam"
    print(find_palindromes(sample_text))