def contains_special_characters(text):
    for char in text:
        if not char.isalnum() and char != ' ':
            return True
    return False

if __name__ == '__main__':
    sample_text = "Hello World! 123"
    result = contains_special_characters(sample_text)
    print(result)