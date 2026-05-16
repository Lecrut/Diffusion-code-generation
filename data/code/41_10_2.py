def manipulate_case(text, case=None):
    if case is None:
        return text
    text = str(text)
    case = case.lower()
    if case == 'lower':
        return text.lower()
    elif case == 'upper':
        return text.upper()
    elif case == 'title':
        return text.title()
    elif case == 'swap':
        return text.swapcase()
    else:
        return text
if __name__ == '__main__':
    print(manipulate_case("Hello World", "lower"))
    print(manipulate_case("Hello World", "upper"))
    print(manipulate_case("Hello World", "title"))
    print(manipulate_case("Hello World", "swap"))
    print(manipulate_case("Hello World", "invalid"))
    print(manipulate_case("Mixed Case", None))