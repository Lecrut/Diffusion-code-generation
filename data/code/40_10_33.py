def get_first_letters(strings):
    return [s[0] for s in strings if s]

if __name__ == '__main__':
    fruits = ["kiwi", "mango", "nectarine", "orange", ""]
    first_letters = get_first_letters(fruits)
    print(first_letters)