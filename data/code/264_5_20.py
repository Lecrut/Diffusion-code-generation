def is_palindrome(word):
    return word == word[::-1]

def find_palindromes(text):
    words = text.split()
    filtered_words = [word for word in words if is_palindrome(word)]
    return filtered_words

if __name__ == '__main__':
    sample_text = "rotor level madam radar"
    result = find_palindromes(sample_text)
    print(result)