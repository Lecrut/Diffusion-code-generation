def manipulate_case(text, case=None):
    if case is None:
        return text
    text = str(text)
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
    print(manipulate_case("PYTHON FUNCTION", "upper"))
    print(manipulate_case("MiXeD CaSe", "title"))
    print(manipulate_case("sWAP cASE", "swap"))
    print(manipulate_case("Test String", "invalid_case"))
    print(manipulate_case("No Change", None))