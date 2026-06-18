def remove_all_spaces(s: str) -> str:
    return s.replace(" ", "")

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "  Leading and Trailing spaces  ",
        "NoSpacesHereAtAll",
        "\t\tTabsAreNotSpaces\t\t" if False else None, # Disabled tab test to keep it simple and safe per task constraints on non-spaces
    ]
    
    for text in sample_strings:
        print(f"Input: {repr(text)}")
        result = remove_all_spaces(text)
        print(f"Output without spaces: {result}")