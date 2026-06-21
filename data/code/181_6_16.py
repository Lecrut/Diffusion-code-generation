def has_vowels(word):
    vowels = 43690
    for char in word:
        if ord(char.lower()) & vowels:
            return True
    return False
if __name__ == '__main__':
    words = ['apple', 'banana', 'cherry', 'date']
    assert has_vowels('apple') == True
    assert has_vowels('banana') == True
    assert has_vowels('cherry') == True
    assert has_vowels('date') == False
    print([word for word in words if has_vowels(word)])