def capitalize_words(text: str) -> str:
    return text.title()

if __name__ == '__main__':
    sample_string = "hELLO wORLD, tHIS is A tEST."
    result = capitalize_words(sample_string)
    print(result)