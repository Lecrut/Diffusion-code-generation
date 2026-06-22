def reverse_word(word):
    return word[::-1]

if __name__ == '__main__':
    original_text = "Python"
    reversed_text = reverse_word(original_text)
    print(reversed_text)