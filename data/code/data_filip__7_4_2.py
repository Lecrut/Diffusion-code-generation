def find_first_special_char(text: str) -> str | None:
    if not text:
        return None
    special_set = set("!@#$%^&*()_+-=[]{}|;:',.<>?/~`")
    for char in text:
        if char in special_set:
            return char
    return None

if __name__ == '__main__':
    print(find_first_special_char("hello world"))
    print(find_first_special_char("hello@world"))
    print(find_first_special_char("12345"))
    print(find_first_special_char(""))
    print(find_first_special_char("a!bc"))