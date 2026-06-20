def find_first_special_character(text):
    special_characters = set('!@#$%^&*()_+-=[]{}|;:,.<>?/~`"\'')
    for char in text:
        if char in special_characters:
            return char
    return None

if __name__ == '__main__':
    print(find_first_special_character("hello world"))
    print(find_first_special_character("hello, world!"))
    print(find_first_special_character("no special chars here"))
    print(find_first_special_character("@start"))