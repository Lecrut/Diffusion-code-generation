def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    sample_value = "hEllo wOrld"
    result = capitalize_first_letter(sample_value)
    print(result)