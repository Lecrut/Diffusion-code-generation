def capitalize_first_letter(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:]

def run_tests():
    assert capitalize_first_letter("hello") == "Hello"
    assert capitalize_first_letter("world") == "World"
    assert capitalize_first_letter("apple") == "Apple"
    assert capitalize_first_letter("") == ""
    assert capitalize_first_letter("a") == "A"
    assert capitalize_first_letter("ALREADY_CAPITALIZED") == "ALREADY_CAPITALIZED"
    assert capitalize_first_letter("already capitalized") == "Already capitalized"
    assert capitalize_first_letter("123abc") == "123abc"
    assert capitalize_first_letter(" hello") == " hello"

if __name__ == '__main__':
    run_tests()
    print(capitalize_first_letter("python"))
    print(capitalize_first_letter("programming"))
    print(capitalize_first_letter("efficient"))