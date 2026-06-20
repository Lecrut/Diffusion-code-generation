def capitalize_words(text):
    return text.title()

if __name__ == '__main__':
    sample_text = "hELLO wORLD, tHIS is A tEST sTRING."
    result = capitalize_words(sample_text)
    print(result)