SPECIAL_CHARS = set("!@#$%^&*()_+-=[]{}|;:',.<>?/~`")

def contains_special_chars(text: str) -> bool:
    return bool(set(text) & SPECIAL_CHARS)

if __name__ == '__main__':
    print(contains_special_chars("hello world"))
    print(contains_special_chars("hello@world"))
    print(contains_special_chars("12345!"))
    print(contains_special_chars("no special here"))