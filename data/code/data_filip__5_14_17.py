def capitalize_words(text):
    return text.title() if text else text

if __name__ == '__main__':
    sample_text = "hELLO wORLD, tHIS is a TEST string."
    result = capitalize_words(sample_text)
    print(result)