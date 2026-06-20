import string

def remove_vowels(text: str) -> str:
    vowels = set("aeiouAEIOU")
    trans_table = str.maketrans('', '', ''.join(vowels))
    return text.translate(trans_table)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = remove_vowels(sample_text)
    print(result)