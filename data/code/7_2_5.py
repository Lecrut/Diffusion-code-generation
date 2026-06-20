SPECIAL_CHARACTERS = set("!?@#$%^&*()_+-=[]{}|;:'\",.<>/~`\\")

def contains_special_characters(text):
    return bool(set(text) & SPECIAL_CHARACTERS)

if __name__ == '__main__':
    print(contains_special_characters("hello world"))
    print(contains_special_characters("hello world!"))
    print(contains_special_characters("12345"))
    print(contains_special_characters("test@email.com"))
    print(contains_special_characters("no specials here"))
    print(contains_special_characters("@#$%"))