def remove_vowels(text):
    trans = str.maketrans('', '', 'aeiouAEIOU')
    return text.translate(trans)

if __name__ == '__main__':
    result = remove_vowels('Hello World!')
    print(result)