SPECIAL_CHARACTERS = set("!@#$%^&*()_+-=[]{}|;:',.<>?/~`")

def contains_special_characters(text: str) -> bool:
    return bool(set(text) & SPECIAL_CHARACTERS)

if __name__ == '__main__':
    print(contains_special_characters("Hello World"))
    print(contains_special_characters("Hello World!"))
    print(contains_special_characters("Test@123"))
    print(contains_special_characters("NoSpecialChars"))
    print(contains_special_characters("!@#$%"))