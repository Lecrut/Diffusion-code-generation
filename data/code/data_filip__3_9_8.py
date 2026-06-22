def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    table = str.maketrans('', '', vowels)
    return text.translate(table)

if __name__ == '__main__':
    result = remove_vowels("Hello World")
    print(result)