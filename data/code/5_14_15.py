def capitalize_words(text: str) -> str:
    return text.title()

if __name__ == '__main__':
    sample_input = "hELLO wORLD, THIS is A tEST."
    result = capitalize_words(sample_input)
    print(result)