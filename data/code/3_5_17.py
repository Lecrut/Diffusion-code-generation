def remove_vowels(text):
    translator = str.maketrans('', '', 'aeiouAEIOU')
    return text.translate(translator)

if __name__ == '__main__':
    result = remove_vowels('Hello World!')
    print(result)