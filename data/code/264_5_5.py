def filter_palindromes(sentence):
    words = sentence.split()
    palindromes = [word for word in words if word == word[::-1]]
    return palindromes

if __name__ == '__main__':
    sample_text = "radar level civic"
    result = filter_palindromes(sample_text)
    print(result)