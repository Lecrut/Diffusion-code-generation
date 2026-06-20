def contains_special_character(text):
    for char in text:
        if not char.isalnum() and char != ' ':
            return True
    return False

if __name__ == '__main__':
    sample_text = "Hello World!"
    result = contains_special_character(sample_text)
    print(result)