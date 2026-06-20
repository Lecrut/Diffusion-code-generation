def remove_vowels(text: str) -> str:
    vowels = "aeiouAEIOU"
    trans_table = str.maketrans({v: None for v in vowels})
    return text.translate(trans_table)

if __name__ == '__main__':
    result = remove_vowels("Hello World")
    print(result)