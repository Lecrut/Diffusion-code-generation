def capitalize_first_letter(sentence: str) -> str:
    if not sentence:
        return sentence
    return sentence[0].upper() + sentence[1:]

if __name__ == '__main__':
    print(capitalize_first_letter("hello world"))
    print(capitalize_first_letter("python programming"))
    print(capitalize_first_letter("123abc"))
    print(capitalize_first_letter(""))