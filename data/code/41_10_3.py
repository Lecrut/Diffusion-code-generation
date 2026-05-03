def manipulate_case(text, case_type=None):
    if case_type is None:
        return text
    text = str(text)
    if case_type == 'lower':
        return text.lower()
    elif case_type == 'upper':
        return text.upper()
    elif case_type == 'title':
        return text.title()
    elif case_type == 'swap':
        return text.swapcase()
    else:
        return text
if __name__ == '__main__':
    sample1 = "HeLlO wOrLd"
    print(f"Original: '{sample1}'")
    print(f"Lower: {manipulate_case(sample1, 'lower')}")
    print(f"Upper: {manipulate_case(sample1, 'upper')}")
    print(f"Title: {manipulate_case(sample1, 'title')}")
    print(f"Swap: {manipulate_case(sample1, 'swap')}")
    print(f"Invalid Input Test: {manipulate_case(sample1, 'invalid')}")
    sample2 = "tHis iS a TeSt"
    print(f"\nOriginal: '{sample2}'")
    print(f"Lower: {manipulate_case(sample2, 'lower')}")
    print(f"Upper: {manipulate_case(sample2, 'upper')}")
    print(f"Title: {manipulate_case(sample2, 'title')}")
    print(f"Swap: {manipulate_case(sample2, 'swap')}")