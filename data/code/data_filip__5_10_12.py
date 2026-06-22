import string

def capitalize_words(word_list: list[str]) -> list[str]:
    capitalized = []
    for word in word_list:
        if word:
            first_char = word[0].upper()
            rest = word[1:]
            capitalized.append(first_char + rest)
        else:
            capitalized.append(word)
    return capitalized

if __name__ == '__main__':
    words = ['hello', 'world', 'python', 'programming', '']
    result = capitalize_words(words)
    print(result)