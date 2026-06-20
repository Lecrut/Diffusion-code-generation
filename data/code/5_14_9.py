def capitalize_words(text):
    return text.title()

if __name__ == '__main__':
    sample_text = "hELLo wORLD, tHIS iS a tEST."
    result = capitalize_words(sample_text)
    print(result)