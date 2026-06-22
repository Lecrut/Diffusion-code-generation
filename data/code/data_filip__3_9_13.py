def remove_vowels(text: str) -> str:
    trans_table = str.maketrans('', '', 'aeiouAEIOU')
    return text.translate(trans_table)

if __name__ == '__main__':
    result = remove_vowels("Hello World")
    print(result)