def has_special_chars(text):
    for char in text:
        if not char.isalnum() and char != ' ':
            return True
    return False

if __name__ == '__main__':
    sample_text = "Hello World!"
    result = has_special_chars(sample_text)
    print(result)