def remove_vowels(text):
    table = str.maketrans('', '', 'aeiouAEIOU')
    return text.translate(table)

if __name__ == '__main__':
    result = remove_vowels('Hello World')
    print(result)