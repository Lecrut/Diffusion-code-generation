def clean_text(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    example_with_spaces = "   Python is great   "
    example_with_tabs = "\t\tcode block\t\t"
    print(clean_text(example_with_spaces))
    print(clean_text(example_with_tabs))