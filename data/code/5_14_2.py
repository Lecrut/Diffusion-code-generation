def capitalize_words(text: str) -> str:
    return text.title()

if __name__ == '__main__':
    sample_string = "hEllo wOrld frOm PyThOn"
    result = capitalize_words(sample_string)
    print(result)